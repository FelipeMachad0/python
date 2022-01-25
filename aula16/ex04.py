cont = 0
nums = []
while True:
    nums.append(int(input('Digite um número: '))) 
    cont += 1
    if cont == 4:
        break
print(f'Você digitou os valores {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(f'O valor 3 apareceu pela primeira vez na {nums.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print('Os valores pares digitados foram: ', end = '')
for n in nums:
    if n % 2 == 0:
        print(n, end = '  ')