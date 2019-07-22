__Author__ = "Victor de Queiroz"
# -*- coding:UTF-8 -*-
'''
Class for APIv2 Treat Crowd
http://www.threatcrowd.org

This Class return subdomains and emails info

'''

import requests
import json


class Subdomains():

    def getSubdomains(self, domain):
        # get info for domain on threat crowd
        response = requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", params={"domain": domain})

        domain_info = json.loads(response.text)

        if domain_info['response_code'] == '1':
            return domain_info['subdomains']
        else:
            return ""


