km = int(input('Digite a distância da viagem: '))
if km <= 200:
    valor = km * 0.5
else:
    valor = km *0.45
print('O valor da viagem deu R${:.2f}'.format(valor))