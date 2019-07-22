__Author__ = 'Victor de Queiroz'
# -*- coding:UTF-8 -*-
"""
Crawler for jurisprudence. www.jusbrasil.com.br

This is a Brazilian site for lawyers publications about jurisprudence and others informations
such as "diário da união" posts.

This crawler search jurisprudence for CNPJ
(CNPJ is a Brazilian documentation about companies)
"""

# query for search format
# https://www.jusbrasil.com.br/jurisprudencia/busca?q=07.170.938%2F0001-07
# format cnpj reciverd = 07.170.938/0001-07
# format query serch cnpj = 07.170.938%2F0001-07

import urllib.request
from bs4 import BeautifulSoup


class Jurisprudence(object):

    def jurisprudence(self, cnpj):
        # replace / to %2F on cnpj
        sub = "/"
        for i in range(0, len(sub)):
            cnpj = cnpj.replace(sub[i], "%2F")

        req = urllib.request.Request(
            url="https://www.jusbrasil.com.br/jurisprudencia/busca?q=" + cnpj,
            data=None,
            headers={
                'User-Agent': 'SPO - sneak peak OSINT https://github.com/victordequeiroz/SPO-Sneak-Peek-OSINT'
            }
        )

        # connect to jusbrasil for request a html content
        with urllib.request.urlopen(req) as url:
            # open html
            url_dump = url.read()

        # instance of beautifulsoup
        soup = BeautifulSoup(url_dump, "lxml")

        # search div class "i juris" on url_dump
        result_not_treated = soup.findAll("div", {"class": "i juris"})

        # treat result_not_treated for show date of jurisprudence and link to show
        # initializate data_trated
        data_treated = {}
        # initialize link list
        links_number_pages = {}

        # update data_treated with link and data_link extrated from beautifulsoup
        for i in range(len(result_not_treated)):
            link = str(result_not_treated[i].find_all("a"))
            link = link.replace("<a href=\"", "")
            link = link.split("\"")
            link = link[0]
            link = link.replace("[", "")
            data_link = str(result_not_treated[i].find_all("p", {"class": "info"}))
            data_link = data_link.replace("<p class=\"info\"> ", "")
            data_link = data_link.replace(" </p>", "")
            data_link = data_link.replace("Data de publicação: ", "")
            data_link = data_link.replace("[ ", "")
            data_link = data_link.replace(" ]", "")
            if data_link in data_treated:
                data_treated.update({data_link + "(" + str(i) + ")": link})
            data_treated.update({data_link: link})

        # search number of pages on result and create a links for crawler
        links_of_pages_not_treated = soup.findAll("a", {"class": "number"})
        if links_of_pages_not_treated:

            # get last page
            number = len(links_of_pages_not_treated)
            links_of_pages_not_treated = links_of_pages_not_treated[number - 1]
            links_of_pages_last = str(links_of_pages_not_treated).replace("<a class=\"number\"", "")
            links_of_pages_last = links_of_pages_last.replace("data-filter-name=\"page\"", "")
            links_of_pages_last = links_of_pages_last.replace("data-filter-value=\"", "")
            links_of_pages_last = links_of_pages_last.replace("rel=\"nofollow\">", "")
            links_of_pages_last = links_of_pages_last.replace("</a>", "")
            links_of_pages_last = links_of_pages_last.replace("\"", "")
            links_of_pages_last = links_of_pages_last.split()
            links_of_pages_last = links_of_pages_last[1]
            links_of_pages_last = links_of_pages_last.replace("href=", "")
            links_of_pages_last = links_of_pages_last.replace("&amp", "&p=")
            links_of_pages_last = links_of_pages_last.split(";")
            last_page = links_of_pages_last[1].split("p=")

            # create a list for urls
            for i in range(int(last_page[1]) + 1):
                if i == 0:
                    i += 1
                links_number_pages.update({i: "https://www.jusbrasil.com.br" + links_of_pages_last[0] + str(
                    i) + "&amp%3B" + str(links_of_pages_last[1])})

        if links_number_pages:
            req = urllib.request.Request(
                url=links_number_pages[i],
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )

            # connect to jusbrasil for request a html content
            with urllib.request.urlopen(req) as url:
                # open html
                url_dump = url.read()

            # instance of beautifulsoup
            soup = BeautifulSoup(url_dump, "lxml")

            # search div class "i juris" on url_dump
            result_not_treated = soup.findAll("div", {"class": "i juris"})

            # treat result_not_treated for show date of jurisprudence and link to show
            # update data_treated with link and data_link extrated from beautifulsoup
            for i in range(len(result_not_treated)):
                link = str(result_not_treated[i].find_all("a"))
                link = link.replace("<a href=\"", "")
                link = link.split("\"")
                link = link[0]
                link = link.replace("[", "")
                data_link = str(result_not_treated[i].find_all("p", {"class": "info"}))
                data_link = data_link.replace("<p class=\"info\"> ", "")
                data_link = data_link.replace(" </p>", "")
                data_link = data_link.replace("Data de publicação: ", "")
                data_link = data_link.replace("[ ", "")
                data_link = data_link.replace(" ]", "")
                if data_link in data_treated:
                    data_treated.update({data_link + "(" + str(i) + ")": link})
                data_treated.update({data_link: link})
            return data_treated
        else:
            return data_treated

