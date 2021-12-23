import random
from time import sleep
opcao_robo = random.randint(1,3)
print('Vamos jogar pedra, papel ou tesoura?')
opcao = int(input('''[1] pedra
[2] papel
[3] tesoura
'''))
print('Pedra,')
sleep(1)
print('Papel,')
sleep(1)
print('Tesoura!')
sleep(1)
if opcao_robo == 1:
    print('O robô escolheu pedra')
    if opcao == 2:
        print('Você ganhou!!')
    elif opcao == 3:
        print('Eu ganhei! Os robôs são superiores aos seres humanos')
elif opcao_robo == 2:
    print('O robô escolheu papel')
    if opcao == 3:
        print('Você ganhou!!')
    elif opcao == 1:
        print('Eu ganhei! Os robôs são superiores aos seres humanos')
else:
    print('O robô escolheu tesoura')
    if opcao == 1:
        print('Você ganhou!!')
    elif opcao == 2:
        print('Eu ganhei! Os robôs são superiores aos seres humanos')
if opcao_robo == opcao:
    print('Empate')
