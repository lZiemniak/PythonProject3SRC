from datetime import *
from hashMdp import *
import os


class Salarie:
    def __init__(self, id,name,firstName,age,mail,function,workgroup,login,passwd,appAdmin,dateCreation,idEntreprise):
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
        self.dateCreation = dateCreation
        self.idEntreprise = idEntreprise
        self.dateLastModif = date.today().strftime("%d/%m/%Y")
	

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getMail(self):
        return self.mail

    def setMail(self, mail):
        self.mail = mail

    def getFunction(self):
        return self.function

    def setFunction(self, function):
        self.function = function

    def getWorkgroup(self):
        return self.workgroup

    def setWorkgroup(self, workgroup):
        self.workgroup = workgroup

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login
        
    def getPasswd(self):
        return self.passwd

    def setPasswd(self,passwd):
        self.passwd = passwd

    def isAppAdmin(self):
        return self.appAdmin

    def setAppAdmin(self,appAdmin):
        self.appAdmin = appAdmin

    def getDateCreation(self):
        return self.dateCreation

    def setDateCreation(self, dateCreation):
        self.dateCreation = dateCreation

    def getDateLastModif(self):
        today= date.today()
        today = today.strftime("%d/%m/%Y")
        self.dateLastModif = today
    
    def getIdEntreprise(self):
        return self.idEntreprise

    def setIdEntreprise(self,idEntreprise):
        self.idEntreprise = idEntreprise

    def toString(self):
        return str(self.id) + ","+self.name + "," +self.firstName + "," +str(self.age) + ","+self.mail+","+self.function+","+self.workgroup+","+self.login+","+self.passwd.decode("ISO-8859-1").encode("unicode_escape").decode("raw_unicode_escape")+","+str(self.appAdmin)+","+self.dateCreation+","+str(self.idEntreprise)
    
    

class Entreprise:
    def __init__(self,companyID,companyName,companyLogo,companyDirector,companyCreationDate):
        self.companyID = companyID
        self.companyName = companyName
        self.companyLogo = companyLogo
        self.companyDirector = companyDirector
        self.companyCreationDate = companyCreationDate
        self.companyEmployeesNum = 0
        self.companyLastModificationDate = date.today().strftime("%d/%m/%Y")

    def getCompanyID(self):
        return self.companyID

    def getCompanyName(self):
        return self.companyName

    def setCompanyName(self, companyName):
        self.companyName = companyName

    def getCompanyLogo(self):
        return self.companyLogo

    def setCompanyLogo(self, companyLogo):
        self.companyLogo = companyLogo

    def getCompanyDirector(self):
        return self.companyDirector

    def setCompanyDirector(self, companyDirector):
        self.companyDirector = companyDirector

    def getCompanyCreationDate(self):
        return self.companyCreationDate

    def setCompanyCreationDate(self, companyCreationDate):
        self.companyCreationDate = companyCreationDate

    def getCompanyEmployeesNum(self):
        return self.companyEmployeesNum

    def setCompanyEmployeesNum(self,companyEmployeesNum):
        self.companyEmployeesNum = companyEmployeesNum

    def addEmployeeToCompany(self):
        self.companyEmployeesNum = self.companyEmployeesNum +1

    def toString(self):
        return str(self.companyID) + ","+self.companyName + "," + self.companyLogo + "," + str(self.companyDirector)+","+str(self.companyEmployeesNum) +","+self.companyCreationDate+"\n"
    


