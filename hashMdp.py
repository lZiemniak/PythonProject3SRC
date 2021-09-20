import hashlib
import binascii
import os

#!!!!!!!!!!!!!!!!!!!!!!!!
#!Code pas encore testé!!
#!!!!!Code à tester!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!



#Hashage du mot de passe
def hashMdp(passwd):
    clef = hashlib.sha256(os.urandom(24)).hexdigest().encode("ascii")
    passwd_hash = hashlib.pbkdf2_hmac("sha256",passwd.encode("utf-8"), clef, 100000)
    passwd_hash = binascii.hexlify(passwd_hash)
    return(clef+passwd_hash).decode("ascii")

#Vérification du bon mot de passe entrée
def checkMdp(mdp_stored, user_passwd):
    clef = mdp_stored[:24]
    mdp_stored = mdp_stored[24:]
    passwd_hash = hashlib.pbkdf2_hmac("sha256", user_passwd.encode("utf-8"),clef.encode("ascii"),100000)
    passwd_hash = binascii.hexlify(passwd_hash).decode("ascii")
    return passwd_hash == user_passwd