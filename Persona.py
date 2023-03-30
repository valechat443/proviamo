class Persona:
    def __init__(self,nome,cognome) :
        self.__nome=nome
        self.__cognome=cognome
        
    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def setNome(self,st):
        self.__nome=st
    def setCognome(self,st):
        self.__cognome=st
        
    def __str__(self) :
        return "nome: "+self.__nome+"\ncognome: "+self.__cognome