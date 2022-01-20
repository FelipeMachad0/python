preco_total = produtos_1000 = menor_preco = 0
while True:
    nome_produto = str(input('Insira o nome do produto: '))
    preco_produto = float(input('Insira o preço do produto: R$'))
    preco_total += preco_produto
    if preco_produto > 1000:
        produtos_1000 += 1
    if menor_preco == 0:
        menor_preco = preco_produto
        nome_menor_preco = nome_produto
    elif preco_produto < menor_preco:
        menor_preco = preco_produto
        nome_menor_preco = nome_produto
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
        print('Opção inválida')
    if continuar == 'N':
        break
print(f'O total da compra foi R${preco_total:.2f}')
print(f'Temos {produtos_1000} produtos custando mais de R$1000.00')
print(f'O produto com o menor preço foi o/a {nome_menor_preco} custando R${menor_preco:.2f}')
