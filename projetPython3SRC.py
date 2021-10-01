#Projet Python Groupe 12
#Christophe Guzik et Léonard Ziemniak

#! /usr/local/bin/python
# coding: utf-8

######################
import os
from hashMdp import *
from ClassFile import *
from datetime import datetime

def getSalarieList():
    f = open("salarie.csv","r")
    listeDeSalaries = []
    for ligne in f:
        splittedLigne = ligne.split(",")
        listeDeSalaries.append(Salarie(splittedLigne[0],
                               splittedLigne[1],
                               splittedLigne[2],
                               splittedLigne[3],
                               splittedLigne[4],
                               splittedLigne[5],
                               splittedLigne[6],
                               splittedLigne[7],
                               splittedLigne[8],
                               splittedLigne[9] ) )
    return listeDeSalaries

def getEntrepriseList():
    f = open("entreprises.csv","r")
    listeDEntreprises = []
    for ligne in f:
        splittedLigne = ligne.split(",")
        listeDEntreprises.append(Entreprise(splittedLigne[0],
                               splittedLigne[1],
                               splittedLigne[2],
                               splittedLigne[3],
                               splittedLigne[4],
                               splittedLigne[5] ) )
    return listeDEntreprise



def connexion(listeDeSalaries):
    connexionOk = False
    salarieReturn = None
    while(connexionOk == False):
        print("Veuillez insérer vos identifiants pour vous connecter: ")
        login = input("Veuillez entrer le login: ")
        mdp = input("Entrez votre mot de passe: ")
        mdp = hashMdp(mdp)
        for unElem in ListeDeSalaries:
            if unElem.getLogin() == login:
                result = checkMdp(mdp, unElem.getPasswd())
                if result == True:
                    salarieReturn = unElem
                    print(salarieReturn)
                    connexionOk = True
                    break
                else:
                    print("Le mot de passe n'est pas Correct")
                    break
        print("Le compte n'a pas été trouvé. Veuillez tenter de se connecter a nouveau.")
    return salarieReturn
        

if __name__ == "__main__":
    listeDeSalaries = getSalarieList()
    listeDEntreprises = getEntrepriseList()

    print("Bienvenue dans l'Active Directory du groupe 12 !")
    
    connexion(listeDeSalaries)
    
    

##    salarieTest = Salarie(1,"Christophe","Bouton",20,"cgpsp6@gmail.com","Débile",12,"cguzik","azerty",True)
##    print(salarieTest.getPasswd())

