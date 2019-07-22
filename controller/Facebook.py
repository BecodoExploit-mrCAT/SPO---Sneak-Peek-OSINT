__Author__ = 'Victor de Queiroz'
"""
Class for facebook search.
On this class we can search a personal info from facebook

+-------------------------------------------------------+
Profile search
https://facebook.com/name.profile-search.example
+-------------------------------------------------------+
About
https://facebook.com/name.profile-search.example/about
[*] overview
[*] work and education
[*] places he's lived
[*] contacts and basic info
[*] family and relationships
[*] details about example
[*] life events
+-------------------------------------------------------+
Friends
https://facebook.com/name.profile-search.example/friends
* This topics can change *
[*] All Friends
[*] Mutual Friends
[*] College 
[*] High School
[*] Current City
[*] More
+-------------------------------------------------------+
Likes
https://facebook.com/name.profile-search.example/likes
+-------------------------------------------------------+
Photos
https://facebook.com/name.profile-search.example/photos
+-------------------------------------------------------+
Videos
https://facebook.com/name.profile-search.example/videos
+-------------------------------------------------------+
CheckIns
https://facebook.com/name.profile-search.example/map
+-------------------------------------------------------+
Sports
https://facebook.com/name.profile-search.example/sports
+-------------------------------------------------------+
Music
https://facebook.com/name.profile-search.example/music
+-------------------------------------------------------+
TV
https://facebook.com/name.profile-search.example/tv
+-------------------------------------------------------+
Movies
https://facebook.com/name.profile-search.example/movies
+-------------------------------------------------------+
Books
https://facebook.com/name.profile-search.example/books
+-------------------------------------------------------+
Events
https://facebook.com/name.profile-search.example/events
+-------------------------------------------------------+

+-------------------------------------------------------+
Search post about company
https://www.facebook.com/search/str/<name+of+company>/keywords_blended_posts
+-------------------------------------------------------+

"""

import urllib.request
from bs4 import BeautifulSoup

class Facebook():

    def __init__(self):
        return self

    # Search information about hometown, current city and jobs from facebook
    def location_by_facebook(profile):
        # create headers
        req = urllib.request.Request(
            url="https://www.facebook.com/" + profile + "/about",
            data=None,
            headers={
                'User-Agent': 'SPO - sneak peak OSINT https://github.com/victordequeiroz/SPO-Sneak-Peek-OSINT'
            }
        )

        # connects on facebook and save untretreated data
        with urllib.request.urlopen(req) as url:
            # open html
            url_dump = url.read()

        # instance of beautifulsoup
        soup = BeautifulSoup(url_dump, 'lxml')

        # work and education
        we_untreated = soup.findAll("div", {"class": "_6a _6b"})
        # initialize we_list for treat
        we_list = []

        for i in range(len(we_untreated)):
            if i % 2 == 1:
                # convert to string for split
                treat = str(we_untreated[i])
                # remove html such as <div class="_6a _6b"><div class="_2lzr _50f5 _50f7">
                treat = treat.replace("<div class=\"_6a _6b\"><div class=\"_2lzr _50f5 _50f7\">", "")
                treat = treat.replace("</a></div><div class=\"_173e _50f8 _2ieq\"><div class=\"fsm fwn fcg\">", " : ")
                treat = treat.replace("<span aria-hidden=\"true\" role=\"presentation\"> · </span>", " : ")
                treat = treat.replace("<div class=\"_6a _6b", "")
                treat = treat.replace("<span class=\"_2iel _50f7", "")
                treat = treat.replace("</div>", "")
                treat = treat.replace("<a href=\"", "")
                treat = treat.replace("\">", " : ")
                treat = treat.replace("</a>", "")
                treat = treat.replace("</span><div class=\"fsm fwn fcg ", " ")
                treat = treat.replace(
                    " : <div class=\"profileFriendsContent : <div class=\"profileFriendsText : <strong>",
                    "&")
                treat = treat.replace(" <a class=\"_39g5\" href=\"", " | ")
                treat = treat.replace("<div class=\"_3-8w _50f8 ", " ")
                # add treated on we_list
                we_list.append(treat)

        location = {}

        for i in range(len(we_list)):
            test = str(we_list[i])
            if test[0] != "&":
                # split per : for treat data
                test = test.split(":")
                # insert atual location and hometown
                if test[0] == " ":
                    location.update({test[5]: test[4]})
                    pass

        return location

    # Get profile picture, and returns on html format in str
    def perfil_picture(profile):
        # create headers
        req = urllib.request.Request(
            url="https://www.facebook.com/" + profile + "/about",
            data=None,
            headers={
                'User-Agent': 'SPO - sneak peak OSINT https://github.com/victordequeiroz/SPO-Sneak-Peek-OSINT'
            }
        )

        # connects on facebook and save untretreated data
        with urllib.request.urlopen(req) as url:
            # open html
            url_dump = url.read()

        # instance of beautifulsoup
        soup = BeautifulSoup(url_dump, 'lxml')

        # parse information on class="photoContainer"
        data = soup.findAll("div", {"class": "photoContainer"})

        profile_picture = str(data)
        profile_picture = profile_picture.replace("[", "")
        profile_picture = profile_picture.replace("]", "")
        return profile_picture

    # Search information about likes
    def likes(profile):
        # create headers
        req = urllib.request.Request(
            url="https://www.facebook.com/" + profile + "/likes",
            data=None,
            headers={
                'User-Agent': 'SPO - sneak peak OSINT https://github.com/victordequeiroz/SPO-Sneak-Peek-OSINT'
            }
        )

        # connects on facebook and save untretreated data
        with urllib.request.urlopen(req) as url:
            # open html
            url_dump = url.read()

        # instance of beautifulsoup
        soup = BeautifulSoup(url_dump, 'lxml')

        # parse information on class="uiCollapsedList uiCollapsedListHidden uiCollapsedListNoSeparate pagesListData"
        data_untreated = soup.findAll("div")

        data_untreated = str(data_untreated)

        data_untreated = data_untreated.replace("href", "*")
        data_untreated = data_untreated.replace("</a>,", " ")
        data_untreated = data_untreated.replace("\">", " : ")
        data_untreated = data_untreated.split("<a")

        # initialize data treated
        data_treated = []

        # show only links
        for i in range(len(data_untreated)):
            if "*=" in data_untreated[i] and not "class" in data_untreated[i] and not "<" in data_untreated[i]:
                treat = str(data_untreated[i]).replace("*=\"", "")
                data_treated.append(treat)

        return data_treated



