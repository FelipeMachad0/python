dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km vc andou? '))
total = 60*dias + 0.15*km
print('O total é pagar é R${:.2f}'.format(total))