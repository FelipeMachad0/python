valor_total = int(input('Qual valor ira sacar? R$'))
cedula50 = cedula20 = cedula10 = cedula5 = moeda1 = 0
while True:
    if valor_total >= 50:
        cedula50 += 1
        valor_total -= 50
    elif valor_total >= 20:
        cedula20 += 1
        valor_total -= 20
    elif valor_total >= 10:
        cedula10 += 1
        valor_total -= 10
    elif valor_total >= 5:
        cedula5 += 1
        valor_total -= 5
    elif valor_total >= 1:
        moeda1 += 1
        valor_total -= 1
    else:
        break
if cedula50 > 0:
    print(f'Cedulas R$50: {cedula50}')
if cedula20 > 0:
    print(f'Cedulas R$20: {cedula20}')
if cedula10 > 0:
    print(f'Cedulas R$10: {cedula10}')
if cedula5 > 0:
    print(f'Cedulas R$5: {cedula5}')
if moeda1 > 0:
    print(f'Moedas R$1: {moeda1}')
