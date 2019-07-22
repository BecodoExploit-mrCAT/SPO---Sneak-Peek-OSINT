__Author__ = 'Victor de Queiroz'
"""
Class for search subdomains on Virus Total
https://developers.virustotal.com/v2.0/reference#api-responses

"""

import requests


class VirusTotal():

    def searchDomain(self, ip):
        # key from virus total search
        virus_total_key = '086176161b18ee281fd2fecb9875545f87557f40b43579cd13034d71a39b63ad'

        # parameters
        params = {'apikey': virus_total_key, 'url': ip}

        # link for search on virus total
        url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'

        params = {'apikey': virus_total_key, 'ip': ip}

        # response for api
        response = requests.get(url, params=params)

        # save json on data_not_treated
        data = response.json()
        data_not_treated = data['resolutions']

        # initialize data_treated
        data_treated = []

        # treated to return resolutions only
        for i in range(len(data_not_treated)):
            data_treated.append(data_not_treated[i]['hostname'])

        return data_treated


