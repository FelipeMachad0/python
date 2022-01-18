rep = soma = 0
n = 1
while n != 0:
    n = int(input('Digite um número (0 para parar):'))
    rep += 1
    soma += n
rep -= 1
print('Você digitou {} números e a soma dos valores foi {} (desconsidere o 0)'.format(rep, soma))
