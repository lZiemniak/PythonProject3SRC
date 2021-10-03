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
    f = open("C:\\Users\\Ekzzin\\Desktop\\pythonProject\\salaries.csv","r", encoding="utf-8")
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
    f = open("C:\\Users\\Ekzzin\\Desktop\\pythonProject\\entreprises.csv","r")
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
    tentativesCo = 0
    while(connexionOk == False):
        if tentativesCo ==3:
            print("Trop de tentatives, arrêt du programme.")
            quit()
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
                    tentativesCo = tentativesCo+1
                    break
        if found == False:
            print("Le compte n'a pas été trouvé. Veuillez tenter de se connecter a nouveau.")
    return salarieReturn



def sauvegardeDonnéesFinDExecution(listSalaries,listEntreprises):
    f = open("salaries.csv","w", encoding="utf-8")
    for uneLigne in listSalaries:
        f.write(uneLigne.toString())
    f.close()
    f = open("entreprises.csv","w")
    for uneLigne in listEntreprises:
        f.write(uneLigne.toString())
    f.close()

def menuAdmin(listeDeSalaries, listeDEntreprises, userConnecte):
    print("Bienvenue sur votre menu "+userConnecte.getFirstName() + " " + userConnecte.getName()+"\n")
    print("Voici la liste des entreprises :" "\n")
    for ligne1 in listeDEntreprises:
        print(str(ligne1.getCompanyID()) + " : " + ligne1.getCompanyName())
        
    print("\nM pour modifier l'utilisateur en cours")
    print("A pour afficher les informations de l'utilisateur connecté")
    print("Tapez Q pour quitter")
    selection = input("\n""Veuillez séléctionner l'identifiant de l'entreprise dont vous souhaitez accéder : ")
    if type(selection) == int:
        entrepriseFound = trouverEntreprise(selection, listeDEntreprises)
        if entrepriseFound != False:
            print("Entreprise trouvée")
            print(entrepriseFound.toString())
        else:
            print("Entreprise inconnue")
    else:
        if selection == 'A' or selection == 'a':
            print(userConnecte.toString())
        elif selection == 'M' or selection == 'm':
            print(userConnecte.toString())
            userConnecte = menuModifUser(userConnecte)
        elif selection == 'Q' or selection == 'q':
            return
 
def menuEntreprise(entreprise):
    

def trouverEntreprise(entrepriseSelec, listeDEntreprises):
    found = False   
    for ligne in listeDEntreprises:
        if int(entrepriseSelec) == ligne.getCompanyID():
            found = True
            return ligne
    return found

                    

#    for ligne3 in f2:
#        splittedLigne3 = ligne3.split(",")
#        if splittedLigne3[0] == entrepriseSelec:
#            os.system("cls")
#            result="\nBienvenue sur le menu de "+splittedLigne3[1]+"\n1 - Liste des salariés\n2 - Modifier les informations de l'entreprise\n3 - Supprimer l'entreprise (attention hein :))"
#            print(listeDeSalaries)
#    print(result)

if __name__ == "__main__":
    listeDeSalaries = getSalarieList()
    listeDEntreprises = getEntrepriseList()
    
    
#    print("Bienvenue dans l'Active Directory du groupe 12 !")
    
    userConnecte = connexion(listeDeSalaries)

#    print("Vous vous etes Connectés! GG")
#    print("Bonjour, " + userConnecte.getFirstName() + " " + userConnecte.getName())
    
    menuAdmin(listeDeSalaries, listeDEntreprises, userConnecte)    
    
    sauvegardeDonnéesFinDExecution(listeDeSalaries, listeDEntreprises)
