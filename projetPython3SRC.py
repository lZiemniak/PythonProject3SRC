#Projet Python Groupe 12
#Christophe Guzik et Léonard Ziemniak

#! /usr/local/bin/python
# coding: utf-8

######################
import os
import psycopg2
from hashMdp import *
from datetime import datetime

##Check si psycop2 est installé ou non
def psycopg2Install():
    cherche = os.system("pip list | findstr psycopg2")
    if cherche == False:
        pass
    else:
        os.system('setx PATH "%PATH%;C:\Python38')
        os.system('setx PATH "%PATH%;C:\Python38\Scripts')
        os.system("py -m pip install --upgrade pip")
        os.system("py -m pip install --upgrade pip --user")
        os.system("pip3 install psycopg2")
    
##Replace login and Password with current superadmin posgresql user
def postgresInit():
    try:
        connexion = psycopg2.connect("dbname=project user=userProject password=azerty")
        cur = connexion.cursor()
        return cur
    except:
        connexion = psycopg2.connect("dbname=postgres user=postgres password=azerty")
        cur = connexion.cursor()
        cur.execute("CREATE DATABASE project")
        cur.execute("CREATE ROLE userProject WITH PASSWORD 'azerty' CREATEDB CREATEROLE LOGIN")
        cur.execute("ALTER DATABASE project OWNER TO project")
        cur.execute("\i initBdd.sql")
        connexion.close()
        postgresInit()

class Salarie:
    def __init__(self, id,name,firstName,age,mail,function,workgroup,login,passwd,appAdmin):
        self.id = id
        self.name = name
        self.firstName = firstName
        self.age = age
        self.mail = mail
        self.function = function
        self.workgroup = workgroup
        self.login = login
        self.passwd = hashMdp(passwd)
        self.appAdmin = appAdmin

    def getId(self):
        return self.id

    def getPasswd(self):
        return self.passwd

class Entreprise:
    def __init__(self,companyID,companyName,companyLogo,companyDirector):
        self.companyID = companyID
        self.companyName = companyName
        self.companyLogo = companyLogo
        self.companyDirector = companyDirector
        self.companyCreationDate = datetime.today().strftime('%Y-%m-%d')
        self.companyEmployeesNum = 0

    


if __name__ == "__main__":


    salarieTest = Salarie(1,"Christophe","Bouton",20,"cgpsp6@gmail.com","Débile",12,"cguzik","azerty",True)
    print(salarieTest.getPasswd())
    
print("Bienvenue dans l'Active Directory du groupe 12 !")
print("Veuillez insérer votre identifiant et votre mot de passe pour vous connecter")
login = input("Indentifiant : ")
passwd = input("Mot de passe : ")
