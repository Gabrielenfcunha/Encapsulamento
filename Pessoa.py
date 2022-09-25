class Pessoa:

    def __init__(self,codigo,nome,endereco,telefone):
        self.__codigo = codigo
        self.nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def getcodigo(self):
            return self.__codigo
    

    def setcodigo(self,codigo):
            self.__codigo = codigo
    
    def getnome(self):
            return self.nome 
    

    def setnome(self,nome):
            self.nome = nome

    def getcodigo(self):
            return self.__endereco 
    

    def setcodigo(self,endereco):
        self.__endereco = endereco
    
    def getnome(self):
            return self.__telefone 
    

    def setnome(self,telefone):
        self.__telefone = telefone


    def imprimeNome(self):
      print("Codigo:" ,self.__codigo,"\nNome:", self.nome,"\nEndereco",self.__endereco,"\nTelefone",self.__telefone )
