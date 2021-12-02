preco = float(input('quantos R$ custa o produto? R$'))
desconto = float(input('quantos % de desconto você quer dar? '))
descontocalculo = 1 - (desconto/100)
preco_com_desconto = preco*descontocalculo
print('O produto que custava R${:.2f} com {:.0f}% de desconto passou a custar R${:.2f}'.format(preco, desconto, preco_com_desconto))