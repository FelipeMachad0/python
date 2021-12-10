import random
print('=-' * 79)
n = int(input('Vamos jogar ímpar par, você é par, eu sou ímpar, escolha um número de 0 a 10: '))
print('=-' * 79)
n_robo = random.randint(0, 10)
if n > 10 or n < 0:
    print('Número invalido!')
elif (n + n_robo) % 2 == 0:
    print('Eu escolhi {}!\n'.format(n_robo))
    print('Parabéns!! Você ganhou!!')
    print('=-' * 79)
else:
    print('Eu escolhi {}!\n'.format(n_robo))
    print('Eu ganhei!! Os robôs são muito melhores que os humanos!!')
    print('=-' * 79)
