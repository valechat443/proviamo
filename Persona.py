class Persona:
    def __init__(self,nome,cognome,colorCapelli,colorOcchi) :
        self.__nome=nome
        self.__cognome=cognome

        self.__coloreCapelli=colorCapelli
        self.__coloreOcchi=colorOcchi
        
    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def getColoreOcchi(self):
        return self.__coloreOcchi
    def getColoreCapelli(self):
        return self.__coloreCapelli

    def setNome(self,st):
        self.__nome=st
    def setCognome(self,st):
        self.__cognome=st
    def setColoreCapelli(self, colCapel):
        self.__coloreCapelli = colCapel
    def setColoreOcchi(self, colOcchi):
        self.__coloreOcchi = colOcchi


        
    def __str__(self) :
        return "nome: "+self.__nome+"\ncognome: "+self.__cognome