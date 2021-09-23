#Projet Python Groupe 12
#Christophe Guzik et Léonard Ziemniak

#! /usr/local/bin/python
# coding: utf-8

######################
import os
import psycopg2
from hashMdp import *

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
    def __init__(self,companyID,companyName,companyLogo,companyDirector,companyCreationDate,companyEmployeesNum):
        self.companyID = companyID
        self.companyName = companyName
        self.companyLogo = companyLogo
        self.companyDirector = companyDirector
        self.companyCreationDate = companyCreationDate
        self.companyEmployeesNum = companyEmployeesNum


if __name__ == "__main__":


    salarieTest = Salarie(1,"Christophe","Bouton",20,"cgpsp6@gmail.com","Débile",12,"cguzik","azerty",True)
    print(salarieTest.getPasswd())
    
##    print("Veuillez vous connecter")
##    login = input("login :")
##    pwd = input("mot de passe :")
##    sortir = False
##    
##    while sortir == False :
##        choix = input("Entrez le numéro du choix: ")
##        if choix.isdigit() == True:
##            choix = int(choix)
##        else:
##            choix = 0
##        if choix == "" or choix == 0:
##            sortir = True
