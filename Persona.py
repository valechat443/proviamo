class Persona:
    def __init__(self, nome:str, cognome:str, eta:int):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        
    def getNome(self):
        return self.__nome
    
    def getCognome(self):
        return self.__cognome
    
    def getEta(self):
        return self.__eta
    
    def setNome(self,nome):
        self.__nome = nome
        
    def setCognome(self,cognome):
        self.__cognome = cognome
    
    def setEta(self, eta):
        self.__eta = eta
        
    def __str__(self) :
        return "Nome: " + self.__nome + "\nCognome: "+ self.__cognome + "\nEtà: " + str(self.__eta)