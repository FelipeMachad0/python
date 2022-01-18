resultado = 1
num = int(input('Digite um número para calcular seu fatorial: '))
print('{}! = '.format(num), end = '')
while num > 1:
    resultado = resultado * num
    print('{} x'.format(num), end = ' ')
    num = num - 1
print('1 = {}'.format(resultado))
    