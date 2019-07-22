__Author__ = 'Victor de Queiroz'

"""
Class for whois query 

"""

import whois

class Whois():
    # return domain ownership
    def owner(self,domain):

        if domain is None:
            return "Invalid query"
        else:
            # whois domain
            queryResult = whois.whois(domain)
            # dict for get owner name, id (cpf for Brazil) and email
            result = {'owner': queryResult.owner, 'ownerid': queryResult.ownerid, 'owneremail': queryResult.email}
            return result


    # return expiration date, creation date and country
    def domainInfo(self,domain):

        if domain is None:
            return "Invalid query"
        else:
            # whois domain
            queryResult = whois.whois(domain)
            result = {'expires': queryResult.expires, 'country':queryResult.country, 'created':queryResult.created}

            return result


