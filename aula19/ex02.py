from random import randint
cont = 1
dados = {'Pessoa 1': randint(1,6), 
'Pessoa 2': randint(1,6), 
'Pessoa 3': randint(1,6),
'Pessoa 4': randint(1,6)}
for item in sorted(dados, key = dados.get, reverse = True):
    print (f'{cont}º lugar: {item} com {dados[item]}.')
    cont += 1
