__Author__ = 'Victor de Queiroz'

"""
Class for search on shodan using 
an API key

"""
import shodan

class Shodan():
    # function for search on shodan
    def search(self,key,query):

        # Setup the api using the key, if key is none insert a valid key
        if key is None:
            return "Invalid KEY, insert a valid key for shodan"
        else:
            "instance of shodan api key"
            api = shodan.Shodan(key)
            # Search a query using a shodan key
            result = api.search(query)
            # return a query result
            return result



