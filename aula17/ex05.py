cont = cont2 = cont3 = cont4 = cont5 = 0
n = []
par = []
impar = []
while True:
    n.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('A lista completa é: ', end = '')
while True:
    print(n[cont2], end = '  ')
    cont2 += 1
    if cont2 >= len(n):
        break
while cont3 < len(n):
    if n[cont3] % 2 == 0:
        par.append(n[cont3])
    else:
        impar.append(n[cont3])
    cont3 += 1
print()
print('Os números pares são: ', end = '')
while True:
    print(par[cont4], end = '  ')
    cont4 += 1
    if cont4 >= len(par):
        break
print()
print('Os números ímpares são: ', end = '')
while True:
    print(impar[cont5], end = '  ')
    cont5 += 1
    if cont5 >= len(impar):
        break
