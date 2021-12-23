print('{:=^40}'.format(' LOJAS MACHADO '))
valor_compra = float(input('Qual o valor da compra? R$'))
print('escolha a forma de pagamento: ')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] Parcelado no cartão')
opcao = int(input(''))
if opcao == 1:
    preco_final = valor_compra * 0.9
    print('Com o desconto o valor da sua compra passou de R${:.2f} para R${:.2f}'.format(valor_compra, preco_final))
elif opcao == 2:
    preco_final = valor_compra * 0.95
    print('Com o desconto o valor da sua compra passou de R${:.2f} para R${:.2f}'.format(valor_compra, preco_final))
elif opcao == 3:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        preco_final = valor_compra * 1.2 
        valor_parcelado = preco_final / parcelas
        print('Sua compra será parcelada em {}x de R${:.2f} \nSua compra de R${:.2f} vai custar R${:.2f} com juros'.format(parcelas, valor_parcelado, valor_compra, preco_final))
    else:
        valor_parcelado = valor_compra / parcelas
        print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcelas, valor_parcelado))
else:
    print('ATENÇÃO!!! FORMA DE PAGAMENTO INVALIDA!!!')
