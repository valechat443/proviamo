class Persona:
    def __init__(self,nome,cognome,altezza) :
        self.__nome=nome
        self.__cognome=cognome
        self.__altezza=altezza
        
    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def setNome(self,st):
        self.__nome=st
    def setCognome(self,st):
        self.__cognome=st

    def getAltezza(self):
        return self.__altezza
    def setAltezza(self,n):
        self.__altezza=n
        
    def getAltezzaInPiedi(self):
        return self.__altezza*0.0328084
    def __str__(self) :
        return "nome: "+self.__nome+"\ncognome: "+self.__cognome
    
