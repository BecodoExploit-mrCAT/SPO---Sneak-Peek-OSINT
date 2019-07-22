__Author__='Victor de Queiroz'
"""
Class for validate SQL querys for
prevent sql injection

"""

class ValidateSQLI(object):

    #test a string if contents ",',#,=
    #and if return false, the query is god
    def validatorSQLI(self,query):
        if query.find("\'") > 0 or query.find("\"") > 0 or query.find("#") > 0 or query.find("=") > 0:
            return True
        else:
            return False
