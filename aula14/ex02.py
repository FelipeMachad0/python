import random
print('=-' * 50)
n_robo = random.randint(0, 10)
n = int(input('escolhi um número de 0 a 10, tente adivinhar qual é: '))
print('=-' * 50)
num_tent = 1
while n != n_robo:
    num_tent += 1 
    if n <= 10 and n >= 0:
        if n > n_robo:
            n = int(input('Errado, o valor é menor, tente novamente: '))
        else:
            n = int(input('Errado, o valor é maior, tente novamente: '))
        print('=-' * 50)
    else: 
        print('Número invalido!')
        print('=-' * 50)
        if n_robo == 1:
            n = 0
            print('O número escolhido foi definido como 0')
            print('=-' * 50)
        else: 
            n = 1
            print('O número escolhido foi definido como 1')
            print('=-' * 50)

print('Parabéns!! Você ganhou!! Você precisou de {} tentativas'.format(num_tent))