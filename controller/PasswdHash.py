__Author__ = 'Victor de Queiroz'
"""
 Class for hashing the password
 for insert into DB

"""
import hashlib

class PasswdHash(object):

    def hash(self,passwd):
        # create hash sha256 on salt potato
        salt = passwd + "potato"
        hash_passwd = hashlib.sha256(salt.encode()).hexdigest()
        # return the hash
        return hash_passwd