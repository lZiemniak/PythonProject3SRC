import hashlib
import os


#Hashage du mot de passe
def hashMdp(passwd):
    salt=os.urandom(32)
    key = hashlib.pbkdf2_hmac("sha256",passwd.encode("utf-8"),salt,100000)
    return salt+key

#check si mdp correct
def checkMdp(storedPasswd, passwd):
    
    storedSalt = storedPasswd[:32]
    storedKey = storedPasswd[32:]
    passwd = hashlib.pbkdf2_hmac("sha256",passwd.encode("utf-8"),storedSalt,100000)
    passwd = storedSalt+passwd
    if storedPasswd == passwd:
        return True
    else:
        
        return False

