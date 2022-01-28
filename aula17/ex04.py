cont = cont2 = 0
n = []
while True:
    n.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print(f'Você digitou {cont} elementos')
n.sort(reverse = True)
print('Os valores em ordem decrescente é: ', end = '')
while True:
    print(n[cont2], end = '  ')
    cont2 += 1
    if cont2 >= len(n):
        break
print()
if 5 in n:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')
