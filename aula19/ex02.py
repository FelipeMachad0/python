from random import randint
from time import sleep
cont = 1
print('Dados jogados!!!')
dados = {'Pessoa 1': randint(1,6), 
'Pessoa 2': randint(1,6), 
'Pessoa 3': randint(1,6),
'Pessoa 4': randint(1,6)}
for item in sorted(dados, key = dados.get, reverse = True):
    sleep(1)
    print (f'{cont}º lugar: {item} com {dados[item]}.')
    cont += 1
