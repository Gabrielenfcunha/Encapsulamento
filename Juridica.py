from Pessoa import Pessoa


class Juridica:
  def __init__(self,codigo,nome,endereco,telefone,cnpj,inscricaoEstadual,quantiadeFuncionario):
    super().__init__(codigo,nome,endereco,telefone)
    self.__cnpj = cnpj
    self.__inscricaoEstadual = inscricaoEstadual
    self.quantiadeFuncionario = quantiadeFuncionario
 
  def getcnpj(self):
            return self.__cnpj
    

  def setcnpj(self,cnpj):
            self.__cnpj = cnpj
    
  def getinscricaoEstadual(self):
            return self.__inscricaoEstadual 
    

  def setinscricaoEstadual(self,inscricaoEstadual):
            self.__inscricaoEstadual = inscricaoEstadual

  def getquantiadeFuncionario(self):
            return self.quantiadeFuncionario 
    

  def setquantiadeFuncionario(self,quantiadeFuncionario):
        self.quantiadeFuncionario = quantiadeFuncionario

  def emitirNotaFiscal(self):
    return print(f"""
    ---Nota Fiscal---
      \nNome da empresa:"{self.nome},
      \nNome da empresa:"{self.endereco}
      \nNome da Quatidade:"{self.quantiadeFuncionario},
      \nNome da empresa:"{self.cnpj},
      """)
    
  def imprimeCPJ(self):
    super().imprimeNome()
    print("Codigo:" ,self.__cnpj,"\nInscriçao Estadual:", self.__inscricaoEstadual,
    "\nQuantiade de Funcionarioo",self.quantiadeFuncionario)