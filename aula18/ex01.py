cadastro = ['', 0]
dados = []
maiorpeso = [0]
menorpeso = [0]
cont = 0
while True:
    cadastro[0] = str(input('Nome: '))
    cadastro[1] = float(input('peso: '))
    dados.append(cadastro[:])
    if cont == 0:
        maiorpeso[0] = cadastro[1]
        maiorpeso.append(cadastro[0])
    elif maiorpeso[0] < cadastro[1]:
        maiorpeso.clear()
        maiorpeso.append(cadastro[1])
        maiorpeso.append(cadastro[0])
    elif maiorpeso[0] == cadastro[1]:
        maiorpeso.append(cadastro[0])
    if cont == 0:
        menorpeso[0] = cadastro[1]
        menorpeso.append(cadastro[0])
    elif menorpeso[0] > cadastro[1]:
        menorpeso.clear()
        menorpeso.append(cadastro[1])
        menorpeso.append(cadastro[0])
    elif menorpeso[0] == cadastro[1]:
        menorpeso.append(cadastro[0])
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print(f'Ao todo tem {cont} pessoas cadastradas')
print(f'O maior peso foi {maiorpeso[0]}, esse é o peso de {maiorpeso[1:]}')
print(f'O menor peso foi {menorpeso[0]}, esse é o peso de {menorpeso[1:]}')
