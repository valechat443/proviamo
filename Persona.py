class Persona:
    def __init__(self, nome:str, cognome:str, eta:int, altezza: float):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__altezza = altezza
        
    def getNome(self):
        return self.__nome
    
    def getCognome(self):
        return self.__cognome
    
    def getEta(self):
        return self.__eta
    
    def getAltezza(self):
        return self.__altezza
    
    def setNome(self, nome):
        self.__nome = nome
        
    def setCognome(self, cognome):
        self.__cognome = cognome
    
    def setEta(self, eta):
        self.__eta = eta
    
    def setAltezza(self, altezza):
        self.__altezza = altezza
    
    def getAltezzaInPiedi(self):
        return self.__altezza*0.0328084
        
    def __str__(self) :
        return "Nome: " + self.__nome + "\nCognome: "+ self.__cognome + "\nEtà: " + str(self.__eta) + "\nAltezza in cm: " + str(self.__altezza)