peso_geral = [0, 0, 0, 0, 0]
for c in range(1, 6):
    peso = int(input('Qual o peso da {}ª pessoa? '.format(c)))
    peso_geral[c-1] = peso
peso_geral.sort()
print('A pessoa mais leve pesa {}kg e a mais pesada {}kg'.format(peso_geral[0], peso_geral[4]))
