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

