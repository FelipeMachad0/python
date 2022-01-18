print('~~' * 15)
print('SEQUÊNCIA DE FIBONACCI')
print('~~' * 15)
rep = int(input('Quantos termos você quer mostrar? '))
n1 = 1
n2 = 0
r = 0
print('0 ➡️  ', end = '')
while rep > 0:
    print('{} ➡️'.format(n1), end = '  ')
    r = n1+n2
    n2 = n1
    n1 = r
    rep -= 1
print('FIM')
