#Declaração de variaveis
cont = cont2 = cont3 = cont4 = maior = menor = 0
lista_num = []
pos_maior = []
pos_menor =  []
#verificação maior e menor
while cont < 5:
    num_atual = int(input(f'Digite um número para a posição {cont + 1}: '))
    lista_num.append(num_atual)
    if maior == 0:
        maior = num_atual
        pos_maior.append(cont + 1)
    elif maior < num_atual:
        maior = num_atual
        pos_maior = []
        pos_maior.append(cont + 1)
    elif maior == num_atual:
        pos_maior.append(cont + 1)
    if menor == 0:
        menor = num_atual
        pos_menor.append(cont + 1)
    elif menor > num_atual:
        menor = num_atual
        pos_menor = []
        pos_menor.append(cont + 1)
    elif menor == num_atual:
        pos_menor.append(cont + 1)
    cont += 1
#Mostrando os resultados na tela
print('Os números digitados foram: ', end = '')
while True:
    print(lista_num[cont2], end = '  ')
    cont2 += 1
    if cont2 > 4:
        break
print(f'\nO maior valor foi {maior} nas posições: ', end = '')
while True:
    print(pos_maior[cont3], end = '  ')
    cont3 += 1
    if cont3 >= len(pos_maior):
        break
print(f'\nO menor valor foi {menor} nas posições: ', end = '')
while True:
    print(pos_menor[cont4], end = '  ')
    cont4 += 1
    if cont4 >= len(pos_menor):
        break
