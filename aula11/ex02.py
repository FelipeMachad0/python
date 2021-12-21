num = int(input('Digite um número inteiro: '))
print('''Escolha para qual base numérica vai querer conventer:
[1] binário
[2] octal
[3] hexidecimal''')
base = int(input(''))
if base == 1:
    num_bin = bin(num)[2:]
    print('O número {} em binário ficaria {}'.format(num, num_bin))
elif base == 2:
    num_oct = oct(num)[2:]
    print('O número {} em octal ficaria {}'.format(num, num_oct))
elif base == 3:
    num_hex = hex(num)[2:]
    print('O número {} em hexidecimal ficaria {}'.format(num, num_hex))
else:
    print('Digite uma opção válido')
