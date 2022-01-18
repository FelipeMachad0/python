import random
vitorias = 0
while True:
    print('=-' * 50)
    while True:       
        n = int(input('Vamos jogar ímpar par, escolha um número de 0 a 10: '))
        if n < 10 or n > 0:
            break
        else:
            print('Número invalido!')
    while True:
        par_impar = str(input('Você quer ser ímpar ou par? [I/P] ')).upper()[0]
        if par_impar == 'I' or par_impar == 'P':
            break
    print('=-' * 50)
    n_robo = random.randint(0, 10)
    if par_impar == 'P':
        if (n + n_robo) % 2 == 0:
            print('Eu escolhi {}!\n'.format(n_robo))
            print('Parabéns!! Você ganhou!!')        
            vitorias += 1
        else:
            print('Eu escolhi {}!\n'.format(n_robo))
            print('Eu ganhei!! Os robôs são muito melhores que os humanos!!')
            print('=-' * 50)
            break
    else:
        if (n + n_robo) % 2 != 0:
            print('Eu escolhi {}!\n'.format(n_robo))
            print('Parabéns!! Você ganhou!')
            vitorias += 1
        else:
            print('Eu escolhi {}!\n'.format(n_robo))
            print('Eu ganhei!! Os robôs são muito melhores que os humanos!!')
            print('=-' * 50)
            break
print(f'Você venceu {vitorias} partidas')
