num = int(input('Digite um número: '))
div = 1
for c in range(1, num):
    if num % c == 0:
        div += 1
print('O número {} foi dívisivel {} vezes'.format(num, div))
if div == 2:
    print('É um número primo')
else:
    print('Não é um número primo')
