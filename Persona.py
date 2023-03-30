class Persona:
    def __init__(self,nome,cognome, eta, nazionalita) :
        self.__nome=nome
        self.__cognome=cognome
        self.__eta=eta
        self.__nazionalita=nazionalita
        
    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def getEta(self):
        return self.__eta
    def getNazionalita(self):
        return self.__nazionalita
    def setNome(self,nome):
        self.__nome=nome
    def setCognome(self,cognome):
        self.__cognome=cognome
    def getEta(self, eta):
        self.__eta = eta
    def getNazionalita(self, nazionalita):
        self.__nazionalita = nazionalita
        
        
    def __str__(self) :
        return "nome: "+self.__nome+"\ncognome: "+self.__cognome+"\neta: "+self.__eta+"\nnazionalita: "+self.__nazionalita