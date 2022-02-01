num_cadastrados = [[], [], []]
cont = 1
while cont <= 7:
    num_cadastrados[0].append(int(input(f'Digite o {cont}º valor: ')))   
    if num_cadastrados[0][cont - 1] % 2 == 0:
        num_cadastrados[1].append(num_cadastrados[0][cont-1])
    else:
        num_cadastrados[2].append(num_cadastrados[0][cont-1])
    cont += 1
print(f'Os valores cadastrados foram: {sorted(num_cadastrados[0])}')
print(f'Os valores pares cadastrados foram: {sorted(num_cadastrados[1])}')
print(f'Os valores ímpares cadastrados foram: {sorted(num_cadastrados[2])}')
