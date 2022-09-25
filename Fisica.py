from Pessoa import Pessoa

class Fisica(Pessoa):
  def __init__(self,codigo,nome,endereco,telefone,cpf,peso,idade,altura):
    super().__init__(codigo,nome,endereco,telefone)
    self.__cpf = cpf
    self.idade = idade
    self.peso = peso
    self.altura = altura

  def getcpf(self):
            return self.__cpf
    

  def setcpf(self,cpf):
            self.__cpf = cpf
    
  def getidade(self):
            return self.idade
    

  def setidade(self,idade):
          self.idade = idade

  def calcularImc(self):
    imc = self.peso / self.altura**2
    situacao = self.situacao_por_imc(imc)
    return f"O IMC de {self.peso} kg é de {round(imc)} {situacao}"
  
  def situacao_por_imc(self,imc):
    if imc < 17:
      situacao = 'Muito abaixo do peso'
    elif imc < 18.49:
      situacao = 'Abaixo do peso'
    elif imc < 24.99:
      situacao = 'Peso normal'
    elif imc < 29.99:
      situacao = 'Acima do Peso'
    elif imc < 34.99:
      situacao = 'Obsidade I'
    elif imc < 39.99:
      situacao = 'obsidade II'
    else:
      situacao = 'obsidade III'
    return situacao


  def imprimicpf(self):
    super().imprimeNome()
    print(f"CPF: {self.__cpf},\nIdade: {self.idade}\nPeso: ,{self.peso},Altura: ,{self.altura},\n,{self.calcularImc()}")
 