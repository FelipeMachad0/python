n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1/n2
resto_divisao = n1%n2
divisao_inteira = n1//n2
elevacao = n1**n2
print('o valor somado é: {} \nsubtraído é: {} \nmultiplicado é: {}\ndividido é: {},'.format(soma, subtracao, multiplicacao, divisao), end=' ')
print('divisão inteira é: {}\nresto da divisão é: {}\nelevação é: {}'.format(divisao_inteira, resto_divisao, elevacao))