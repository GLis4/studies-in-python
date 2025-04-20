#manipulação de listas
class Animal():
    def __init__(self, nome):
        self.nome = nome
        
ovelha = Animal('ovelha')
porco = Animal('porco')
leão = Animal('leão')
vaca = Animal('vaca')

lista1 = [ovelha, porco, vaca]
lista2 = [ovelha, porco, leão]

itens_comuns = set(lista1) & set(lista2)

for item in itens_comuns:
    print(item.nome)