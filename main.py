from Pessoa import Pessoa
from Juridica import Juridica
from Fisica import Fisica

Pe = Pessoa(1,"Gabrielen","Alcides Maia",992187791)
Pe.imprimeNome()

print("-="*10)

Ju = Juridica(2,"Festolandia","osvaldo aranha 130",123456,12345,6789,67)
Ju.imprimeCPJ()