cont = 0
produtos = []
while True:
    produtos.append(str(input('Digite um produto: ')))
    produtos.append(float(input('Digite o valor do produto: R$')))
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('-' * 40)
print(f'{"Listagem de preços": ^40}')
print('-' * 40)
while cont < len(produtos):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<30}', end = '')
    else:
        print(f'R${produtos[cont]:>7.2f}')
    cont += 1
