class Fisica:
  def __init__(self,codigo,nome,endereco,telefone,cpf,peso,idade,altura):
    super().__init__(codigo,nome,endereco,telefone)
    self.cpf = cpf
    self.peso = peso
    self.idade = idade
    self.altura = altura

  def getcpf(self):
            return self.cpf
    

  def setcpf(self,cpf):
            self.cpf = cpf
    
  def getidade(self):
            return self.idade
    

  def setidade(self,idade):
          self.idade = idade

  