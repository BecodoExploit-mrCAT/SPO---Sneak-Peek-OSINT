__Author__ = 'Victor de Queiroz'
"""
Class for open connection on mysql
If fisrt access create a DB

"""
import pymysql


class DataFactory(object):
    # global information for sgbd connect
    host = 'localhost'
    user = 'japonesdafederal'
    password = 'aytegs&7s7gj'
    db = 'SPO'


    #for insert querys
    def insert(self,sql):
        #start a connection
        connect = pymysql.connect(self.host,self.user,self.password,self.db,cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:

                cursor.execute(sql)

            # exec a query
            connect.commit()

        finally:
            connect.close()

    #for select specific querys
    def select(self,sql):
        #start connection
        connect = pymysql.connect(self.host,self.user,self.password,self.db,cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:

                cursor.execute(sql)

                result = cursor.fetchone()
                return result

            # exec a query

        finally:
            connect.close()

    # for update querys
    def update(self,sql):
        #start connect
        connect = pymysql.connect(self.host,self.user,self.password,self.db,cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:

                cursor.execute(sql)

            # exec a query
            connect.commit()

        finally:
            connect.close()
