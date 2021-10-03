#Projet Python Groupe 12
#Christophe Guzik et Léonard Ziemniak

#!/usr/bin/env python3
# coding: utf-8

######################
import os
from hashMdp import *
from ClassFile import *
from datetime import *
from getpass import getpass


def getSalarieList():
    f = open("salaries.csv","r", encoding="utf-8")
    listeDeSalaries = []
    for ligne in f:
        splittedLigne = ligne.split(",")
        passwdToFormat = splittedLigne[8]
        password = passwdToFormat.encode("raw_unicode_escape")
        password = password.decode("unicode_escape").encode("ISO-8859-1")        
        listeDeSalaries.append(Salarie(int(splittedLigne[0]),
                               splittedLigne[1],
                               splittedLigne[2],
                               int(splittedLigne[3]),
                               splittedLigne[4],
                               splittedLigne[5],
                               splittedLigne[6],
                               splittedLigne[7],
                               password,
                               bool(splittedLigne[9]),
                               splittedLigne[10],
                               splittedLigne[11] ) )
    return listeDeSalaries

def getEntrepriseList():
    f = open("entreprises.csv","r")
    listeDEntreprises = []
    for ligne in f:
        splittedLigne = ligne.split(",")
        listeDEntreprises.append(Entreprise(int(splittedLigne[0]),
                               splittedLigne[1],
                               splittedLigne[2],
                               int(splittedLigne[3]),
                               splittedLigne[4] ) )
    return listeDEntreprises


def connexion(listeDeSalaries):
    connexionOk = False
    salarieReturn = None
    while(connexionOk == False):
        print("Veuillez insérer vos identifiants pour vous connecter: ")
        login = input("Veuillez entrer le login: ")
        mdp = input("Entrez votre mot de passe: ")
        found = False
        for unElem in listeDeSalaries:
            if unElem.getLogin() == login:
                found = True
                result = checkMdp(unElem.getPasswd(), mdp )
                if result == True:
                    salarieReturn = unElem
                    connexionOk = True
                    break
                else:
                    print("Le mot de passe n'est pas correct")
                    break
        if found == False:
            print("Le compte n'a pas été trouvé. Veuillez tenter de se connecter a nouveau.")
    return salarieReturn

def menuAdmin():
    f1 = open("C:\\Users\\Ekzzin\\Desktop\\pythonProject\\salaries.csv","r")
    with open('C:\\Users\\Ekzzin\\Desktop\\pythonProject\\entreprises.csv') as f2:
    #f2 = open("C:\\Users\\Ekzzin\\Desktop\\pythonProject\\entreprises.csv","r")
        f2list = f2.readlines()
        for ligne1 in f1:
            splittedLigne1 = ligne1.split(",")
            print("Bienvenue sur votre menu",splittedLigne1[1],"\n")
            print("Voici la liste des entreprises :" "\n")
            for ligne2 in f2list:
                splittedLigne2 = ligne2.split(",")
                print(splittedLigne2[0], splittedLigne2[1])
            
        entrepriseSelec = input("\n""Veuillez séléctionner l'identifiant de l'entreprise dont vous souhaitez accéder : ")

        result="L'entreprise n'existe pas"

        for ligne3 in f2list:
            splittedLigne3 = ligne3.split(",")
            if splittedLigne3[0] == entrepriseSelec:
                os.system("cls")
                result="\nBienvenue sur le menu de "+splittedLigne3[1]+"\n1 - Liste des salariés\n2 - Modifier les informations de l'entreprise\n3 - Supprimer l'entreprise (attention hein :))"
        print(result)


if __name__ == "__main__":
    listeDeSalaries = getSalarieList()
    listeDEntreprises = getEntrepriseList()

    
    print("Bienvenue dans l'Active Directory du groupe 12 !")
    
    connexion(listeDeSalaries)

    print("Vous vous etes Connectés! GG")

    
    
    

##    salarieTest = Salarie(1,"Christophe","Bouton",20,"cgpsp6@gmail.com","Débile",12,"cguzik","azerty",True)
##    print(salarieTest.getPasswd())

