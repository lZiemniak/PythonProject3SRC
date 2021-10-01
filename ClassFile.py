import datetime

class Salarie:
    def __init__(self, id,name,firstName,age,mail,function,workgroup,login,passwd,appAdmin,dateCreation):
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
        self.dateCreation = dateCreation
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
    
    
    

class Entreprise:
    def __init__(self,companyID,companyName,companyLogo,companyDirector):
        self.companyID = companyID
        self.companyName = companyName
        self.companyLogo = companyLogo
        self.companyDirector = companyDirector
        self.companyCreationDate = datetime.today().strftime('%Y-%m-%d')
        self.companyEmployeesNum = 0

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

    
