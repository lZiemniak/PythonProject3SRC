#Projet Python Groupe 12
#Christophe Guzik et Léonard Ziemniak

#! /usr/local/bin/python
# coding: utf-8

######################
import os;
import psycopg2;

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
    def __init__(self, id,name,firstName,age,mail,function,workgroup,login,passwd,appAdmin,dateCreation,dateLastModif,id_entreprise):
        self.id = id
        self.name = name
        self.firstName = firstName
        self.age = age
        self.mail = mail
        self.function = function
        self.workgroup = workgroup
        self.login = login
        self.passwd = passwd
        self.appAdmin = appAdmin

    def getId(self):
        return self.id






if __name__ == "__main__":

    print("Veuillez vous connecter")
    login = input("login :")
    pwd = input("mot de passe :")
    

    
    while choix != 0 :
        choix = input("Entrez le numéro du choix: ")
        if choix.isdigit() == True:
            choix = int(choix)
        else:
            choix = 0
        if choix == "":
            choix = 0
