num_array = []
cont = 0
while True:
    num = int(input('Digite um número: '))
    if num in num_array:
        print('Número invalido')
    else:
        num_array.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
num_array.sort()
print('Você digitou os valores: ', end = '')
while True:
    print(num_array[cont], end = '  ')
    cont += 1
    if cont >= len(num_array):
        break
