continuar = 's'
num = []
rep = 0
while continuar == 's':
    num.append(int(input('Digite um número: ')))
    rep += 1
    continuar = str(input('Quer continuar? [S/N] ')).lower()
med = sum(num)/len(num)
num.sort()
print('Você digitou {} números e a média dos valores foi {}'.format(rep, med))
print('O maior número foi {} e o menor {}'.format(num[rep-1], num[0]))
