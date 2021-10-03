#Projet Python Groupe 12
#Christophe Guzik et Léonard Ziemniak

#!/usr/bin/env python3
# coding: utf-8

#####

#Pb a résoudre: pb d'acces au menu entreprise
#fonctionnalités a ajouter: corriger les dates de dernière modif, age en fonction de la date naissance

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
    ok = False
    while ok == False :   
        print("\nM pour modifier l'utilisateur en cours")
        print("A pour afficher les informations de l'utilisateur connecté")
        print("E pour ajouter une nouvelle entreprise")
        print("S pour ajouter un nouveau salarié")
        print("F pour afficher tous les salariés")
        print("D pour supprimér un salarié")
        print("Tapez Q pour quitter")
        
        selection = input("\n""Veuillez séléctionner l'identifiant de l'entreprise ou l'action souhaitée : ")
        try:
            selection = int(selection)
            entrepriseFound = trouverEntreprise(selection, listeDEntreprises)
            if entrepriseFound != False:
                print("Entreprise trouvée")
                menuEntreprise(entreprise,listeDEntreprises)
            else:
                print("Entreprise inconnue")
        except:
            if selection == 'A' or selection == 'a':
                print(userConnecte.toString())
            elif selection == 'M' or selection == 'm':
                print(userConnecte.toString())
                userConnecte = menuModifUser(userConnecte)
            elif selection == "E" or selection == "e":
                print("Ajout de nouvelle entreprise :")
                addNewEntreprise(listeDEntreprises)
            elif selection == "S" or selection == "s":
                print("Ajout d'un nouvel utilisateur")
                creationUser(listeDeSalaries)
            elif selection == "F" or selection == "f":
                for ligne in listeDeSalaries:
                    print(ligne.toString())
            elif selection == "D" or selection == "d":
                userId = int(input("Veuillez entrer l'Id de l'utilisateur a supprimer :"))
                deleteUser(userId, listeDeSalaries)
                
            elif selection == 'Q' or selection == 'q':
                ok = True
            else:
                print("Choix inconnu, Veuillez réésayer.")
    return

def creationUser(listeDeSalaries):
    idS = 0
    for unElem in listeDeSalaries:
        idS = unElem.getId()
    idS = idS+1
    name = input("Entrez nom:")
    firstName = input("Entrez prénom:")
    age = int(input("entrez age:"))
    mail = input("entrez mail:")
    fonction = input("entrez fonction:")
    workgroup = input("entrez workgroup")
    login = generateLogin(name,firstName)
    mdp = input("entrez mot de passe")
    mdp = hashMdp(mdp)
    isAdmin = bool(input("Est ce que l'utilisateur est admin? (True ou False):"))
    creationDate = date.today().strftime("%d/%m/%Y")
    entreprise = int(input("Entrez l'Id de l'entreprise : "))

    listeDeSalaries.append(Salarie(idS,name,firstName,age,mail,fonction,workgroup,login,mdp,isAdmin,creationDate,entreprise))
    print("l'utilisateur a été ajouté.")

def deleteUser(userId,listeDeSalaries):
    good = False
    for i in range(len(listeDeSalaries)):
        if listeDeSalaries[i].getId()==userId:
            del listeDeSalaries[i]
            good = True
    if good == True:
        print("l'utilisateur a été supprimé.")
    else:
        print("Utilisateur inconnu")
    return good

def menuModifUser(user):
    ok = False
    while ok == False:
        print("Modification de l'utilisateur :\n")
        print(user.toString())
        print("\nN pour le nom")
        print("P pour le prénom")
        print("A pour l'age")
        print("M pour le mail")
        print("F pour la fonction")
        print("W pour le groupe de travail")
        print("L pour le login")
        print("P pour le mot de passe")
        print("D pour modifier son paramètre Admin")
        print("E pour modifier son entreprise")
        print("B pour annuler")
        choice = input("Entrez votre choix :")
        if choice == "N" or choice =="n":
            new = input("Entrez le nouveau nom")
        elif choice == "P" or choice =="p":
            new = input("Entrez le nouveau prénom")
        elif choice == "A" or choice =="A":
            new = input("modifier Age")
        elif choice == "M" or choice =="m":
            new = input("Modifier mail")
        elif choice == "F" or choice =="f":
            new = input("Modifier fonction")
        elif choice == "W" or choice =="w":
            new = input("modifier groupe de travail")
        elif choice == "L" or choice =="l":
            new = input("modifier login")
        elif choice == "P" or choice =="p":
            new = input("modifier mot de passe")
        elif choice == "D" or choice == "d":
            new = input("modifier parametre admin")
        elif choice == "E" or choice =="e":
            new = input("modifier Entreprise")
        elif choice == "B" or choice =="b":
            ok = True
            print("Fin de modification.")
        else:
            print("Choix inconnu, veuillez réésayer.")
    return
        
def menuEntreprise(entreprise, listeDEntreprises):
    choice = ""
    while choice != "B" or choice != "b":
        print(entreprise.toString())
        print("M pour modifier")
        print("S pour supprimer")
        print("B pour revenir en arrière")
        choice = input("Veuillez choisir une action pour l'entreprise choisie: ")
        if choice == "M" or choice == "m":
            modifierEntreprise(entreprise)
        elif choice == "S" or choice == "s":
            deleteEntreprise(entreprise, listeDEntreprises)
            print("l'entreprise " + entreprise.getName() + " a été supprimé.")
            return
    return
 

def modifierEntreprise(entreprise):
    ok = False
    entreprise
    print("Voici l'entreprise que vous voulez modifier: ")
    print("-"*10)
    print(entreprise.toString())
    while ok == False:
        print("1 pour modifier le nom")
        print("2 pour modifier le logo")
        print("3 pour modifier le directeur de l'entreprise")
        print("0 pour annuler la modification")
        choice = input("Veuillez choisir: ")
        choice = int(choice)
        if choice == 1:
            newName = input("Veuillez chosisir le nouveau nom:")
            entreprise.setCompanyName(newName)
        elif choice == 2:
            newLogo = input("Veuillez choisir un nouveau logo:")
            entreprise.setCompanyLogo(newLogo)
        elif choice == 3:
            newCEOID = input("Veuillez choisir l'identifiant du nouveau directeur:")
            entreprise.setCompanyDirector(newCEOID)
        elif choice == 0:
            ok = True
        else:
            print("Choix inconnu")
    return

def generateLogin(name,firstName):
    login = firstName.lower()[0] + name.lower()
    return login

def deleteEntreprise(entreprise, listeDEntreprises):
    for i in range(len(listeDEntreprises)):
        if entreprise.getCompanyID() == listeDEntreprises[i].getCompanyID():
            del listeDEntreprises[i]
            return

def trouverEntreprise(entrepriseSelec, listeDEntreprises):
    found = False   
    for ligne in listeDEntreprises:
        if int(entrepriseSelec) == ligne.getCompanyID():
            found = True
            return ligne
    return found



if __name__ == "__main__":
    listeDeSalaries = getSalarieList()
    listeDEntreprises = getEntrepriseList()
    
    
    
    userConnecte = connexion(listeDeSalaries)
    
    print("Bienvenue dans l'Active Directory du groupe 12 !")
    print("Bonjour, " + userConnecte.getFirstName() + " " + userConnecte.getName())
    if userConnecte.isAppAdmin() == True:
        menuAdmin(listeDeSalaries, listeDEntreprises, userConnecte)
    
    print("Au revoir")
    sauvegardeDonnéesFinDExecution(listeDeSalaries, listeDEntreprises)


