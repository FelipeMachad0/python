import random
from time import sleep
jogos_total = []
jogo = []
cont = cont2 = quant_jogos = num_add = 0
print(f'''{'='*20}
     MEGA SENA
{'='*20}''')
quant_jogos = int(input('Quantos jogos você vai querer sortear? '))
while quant_jogos > cont2:
    while cont <= 5:
        num_add = random.randint(1,60)
        while num_add in jogo:
            num_add = random.randint(1,60)
        jogo.append(num_add)
        cont += 1
    jogo.sort()
    cont = 0
    cont2 += 1
    jogos_total.append(jogo)
    jogo = []
while cont < quant_jogos:
    print(f'Jogo {cont + 1}: {jogos_total[cont]}')
    cont += 1
    sleep(1)
print('=-=-=-=-=-BOA SORTE-=-=-=-=-=')
