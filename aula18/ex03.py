matriz = [[],[],[],[],[],[],[],[],[]]
cont = soma_par = soma_terceirac = maior_segundal = 0
while cont <= 8:
    matriz[cont] = int(input(f'Digite um valor para a posição {cont + 1}: '))
    if matriz[cont] % 2 == 0:
        soma_par += matriz[cont]
    if cont == 2 or cont == 5 or cont == 8:
        soma_terceirac += matriz[cont]
    cont += 1
if matriz[3] > matriz[4]:
    if matriz [3] > matriz[5]:
        maior_segundal = matriz[3]
    else:
        maior_segundal = matriz[5]
elif matriz[4] > matriz[5]:
    maior_segundal = matriz[4]
else:
    maior_segundal = matriz[5]
print(f'''[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]
[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]
[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]''')
print(f'A soma dos valores par é {soma_par}')
print(f'A soma da terceira coluna é {soma_terceirac}')
print(f'O maior valor da segunda linha é {maior_segundal}')
