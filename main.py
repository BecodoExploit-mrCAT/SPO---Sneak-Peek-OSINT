# -*- coding:UTF-8 -*-
__author__ = 'Victor de Queiroz'
"""
        
             ██████  ██▓███   ▒█████  
           ▒██    ▒ ▓██░  ██▒▒██▒  ██▒
           ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒
             ▒   ██▒▒██▄█▓▒ ▒▒██   ██░
           ▒██████▒▒▒██▒ ░  ░░ ████▓▒░
           ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ 
           ░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░ 
           ░  ░  ░  ░░       ░ ░ ░ ▒  
                 ░               ░ ░
                   
        S n e a k    P e e k   O S I N T
        
SPO is a software for search OSINT content.
SPO is a opensource code, please don't use this with
other license different than GPLv2.

Developed by Victor de Queiroz
Contact: CATx003@protonmail.com

+------------- ♥ For donations ♥ -----------------+
|                                                 |
| ŁTC = LPE5DsjA2YcMuGGZspvRzEEvdoAjvTRzvF        |
| ɃTC = 1FtBj9QbT7gDcxSCygTnUop4N3bd75bwRZ        |
| ɃCH = qr6gn0r20p9s9kjm5yuvqw53mhmzx87q0vecqn6xhj|
|                                                 |
+-------------------------------------------------+


"""
from datetime import timedelta
from flask import Flask, render_template, url_for, session, request, redirect, flash
from controller import spoDAO
from controller import Whois
from controller import CNPJ
from controller import Jurisprudence
from controller import Subdomain
from controller import Facebook

# spo is a instance of flask,
# template_folder is a directory of contents html sources from view
# static_folder is a static contents like a css, js, etc...
spo = Flask(__name__, template_folder="templates", static_folder="static")
# key of access for wsgi
# use if necessary, we are running spo in a local daemon
# but u can use spo as server, if u don't want use a mod_proxy
# on apache for example, use this key for wsgi
spo.secret_key = 'ˆˆß∂……å¬ßøøøø∑ßˆˆß∆˚¬˜˜≤'

# instance of data access object
dao = spoDAO.SpoDAO()
# instance of Whois
whois = Whois.Whois()
# instance of cnpj api
cnpj = CNPJ.CNPJ()
# instance of jurisprudence
lawyer = Jurisprudence.Jurisprudence()
# instance of subdomains
subdomain = Subdomain.Subdomains()
# instance of Facebook
facebook = Facebook.Facebook

# for timeout session on 2 minutes
@spo.before_request
def make_session_permanent():
    session.permanent = True
    spo.permanent_session_lifetime = timedelta(minutes=15)


# for logout
@spo.route("/exit")
def exit():
    session.pop('user', None)
    return redirect(url_for("login"))


# errors
@spo.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@spo.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@spo.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


"""
+-------------------------------------------------+
|                                                 |
|                 Login screen                    |
|                                                 |
+-------------------------------------------------+
Function that is responsible for managing login and 
user creation for the first access by opening the cookie 
session and dealing with sqli attacks ex: a ' or 1 = 1#
"""


@spo.route("/", methods=['GET', 'POST'])
def login():
    # on first access redirect to firstLogin
    if dao.testFirstAccess() == True:
        return redirect('wellcome')

    else:
        if request.method == 'POST':
            # recive user from html
            getUser = request.form.get('user')
            # recive password from html
            getPasswd = request.form.get('password')

            # test login
            if dao.testLogin(getUser, getPasswd) == True:
                # open a session
                session['user'] = getUser
                session['isAuthenticated'] = True
                session['id'] = dao.getIDUser(getUser)
                return redirect('dashboard')
            else:
                return render_template("passwordFail.html")

        # render login.html
        return render_template("login.html")


# for first login
@spo.route("/wellcome")
def wellcome():
    # wellcome screen
    return render_template('wellcome.html')


@spo.route("/firstLogin", methods=['GET', 'POST'])
def firstLogin():
    if request.method == 'POST':
        # recive user from html
        getUser = request.form.get('user')
        # recive password from html
        getPasswd = request.form.get('password')
        # insert in to DB
        dao.insertUser(getUser, getPasswd)
        return render_template("ok_registration.html")
    return render_template("firstLogin.html")


"""
+-------------------------------------------------+
|                                                 |
|                 User Dashboard                  |
|                                                 |
+-------------------------------------------------+
Function that is responsible for principal page
"""


@spo.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        return render_template("dashboard.html")


"""
+-------------------------------------------------+
|                                                 |
|             Company Investigation               |
|                                                 |
+-------------------------------------------------+
Function that is responsible for start a new Company investigation.
"""
@spo.route("/companyInvestigation", methods=['GET', 'POST'])
def companyInvestigation():
    # test if is authenticated
    if session['isAuthenticated'] == True:

        if request.method == 'POST':
            # start a new project
            nameOfProject = request.form.get('nameOfProject')
            # send a informa
            if request.form.get('domain'):
                # getDomain
                domain_name = request.form.get('domain')
                # get whois info
                ownerDomainInfo = whois.owner(domain_name)

                if ownerDomainInfo['ownerid'] is None:
                    domainInfo = ""
                else:
                    # if owner is cnpj
                    if len(ownerDomainInfo['ownerid']) == 18:
                        # get cnpj info
                        domainInfo = cnpj.getCNPJ(ownerDomainInfo['ownerid'])
                        # get process info
                        process = lawyer.jurisprudence(ownerDomainInfo['ownerid'])
                        # treat cnpj
                        TreatCNPJ = cnpj.treat(ownerDomainInfo['ownerid'])
                        subdomains = subdomain.getSubdomains(domain_name)
                    else:
                        domainInfo = ''

                return render_template('companyInvestigation.html', subdomain=subdomains, domain_name=domain_name,
                                       cnpj=TreatCNPJ, ownerDomainInfo=ownerDomainInfo, domainInfo=domainInfo,
                                       jurisprudence=process)

        return render_template("companyInvestigation.html", subdomain='', domain_name='', ownerDomainInfo='', domainInfo='',
                               jurisprudence="", cnpj="")

"""
+-------------------------------------------------+
|                                                 |
|            Personal Investigation               |
|                                                 |
+-------------------------------------------------+
Function that is responsible for start a new Personal investigation.
"""
@spo.route("/personalInvestigation", methods=['GET','POST'])
def personalInvestigation():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        if request.method == 'POST':
            # for facebook crawler
            profile_facebook = request.form.get('profile_facebook')
            # get profile picture
            photo_perfil = facebook.perfil_picture(profile_facebook)
            # get likes
            likes_by_facebook = facebook.likes(profile_facebook)
            # get location by facebook
            location_by_facebook = facebook.location_by_facebook(profile_facebook)

            return render_template("personalInvestigation.html", photo_perfil=photo_perfil, likes_by_facebook=likes_by_facebook,location_by_facebook=location_by_facebook)






        return render_template("personalInvestigation.html", photo_perfil='', likes_by_facebook='',location_by_facebook='')



"""
+-------------------------------------------------+
|                                                 |
|                 Search Servers                  |
|                                                 |
+-------------------------------------------------+
Function that is responsible for search a servers and services.
Here we'll use the shodan key and others tools for search,
and crawlers and etc.. 
"""


@spo.route("/searchServers")
def searchServers():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        return render_template("searchServers.html")


"""
+-------------------------------------------------+
|                                                 |
|                Personal Trace                   |
|                                                 |
+-------------------------------------------------+
Function that is responsible for search a person, on facebook
instagram, twitter and whatever public data allow on internet 
about especific people.
"""


@spo.route("/personalTrace")
def personalTrace():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        return render_template("personalInvestigation.html")


"""
+-------------------------------------------------+
|                                                 |
|                   About OSINT                   |
|                                                 |
+-------------------------------------------------+
Function about educational articles
"""


@spo.route("/aboutOSINT")
def aboutOSINT():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        return render_template("aboutOSINT.html")


"""
+-------------------------------------------------+
|                                                 |
|                    Manual                       |
|                                                 |
+-------------------------------------------------+
Function for help
"""


@spo.route("/manual")
def manual():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        return render_template("manual.html")


"""
+-------------------------------------------------+
|                                                 |
|                Insert Keys                      |
|                                                 |
+-------------------------------------------------+
Function that is responsible for insert a credentials
for social media when we using for search on crawlers
"""


@spo.route("/insertKeys", methods=['GET', 'POST'])
def insertKeys():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        # test existent keys
        if dao.getShodanKey(session['id']) is None:
            pass
        else:
            flash('Shodan Key inserted: ' + dao.getShodanKey(session['id'])['key_value'], 'info')

        if request.method == 'POST':

            shodanKey = request.form.get('shodan')
            if dao.getShodanKey(session['id']) is None:
                dao.insertShodanKey(session['id'], shodanKey)
                flash('Shodan Key inserted: ' + dao.getShodanKey(session['id'])['key_value'], 'info')
                return redirect('insertKeys')
            else:
                dao.updateShodanKey(session['id'], shodanKey)
                flash('Shodan Key updated: ' + dao.getShodanKey(session['id'])['key_value'], 'info')
                return render_template("insertKeys.html")

        return render_template("insertKeys.html")


"""
+-------------------------------------------------+
|                                                 |
|                   About US                      |
|                                                 |
+-------------------------------------------------+
The best function on this software, because here is
a bitcoin wallet ♥ ♥ ♥ ♥ uheuheuheu 
"""


@spo.route("/about")
def aboutUS():
    # test if is authenticated
    if session['isAuthenticated'] == True:
        return render_template("aboutus.html")


"""
+-------------------------------------------------+
|                                                 |
|                   Run SPO                       |
|                                                 |
+-------------------------------------------------+
Function that is responsible for start SPO, on documentation
is describled how to configure a daemon spod and execute.
We disponibilizing a web service for SPO, send-me a email
for talk about this!
"""
if __name__ == '__main__':
    # spo run in 1337 port tcp
    # For real use disallow debug mode, set False
    spo.run(port=1337, debug=True)
    __author__ = 'Victor de Queiroz'
