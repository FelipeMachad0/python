cont = cont2 = cont4 = cont5 = 0
cont3 = 16
times = ['Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragrantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense']
print('Tabela Brasileirão 2021:', end = ' ')
while True:
    print(times[cont], end=', ')
    cont += 1
    if cont > 19:
        print('')
        break
print('=-' * 30)
print('G4:', end = ' ')
while True:
    print(times[cont2], end=', ')
    cont2 += 1
    if cont2 > 3:
        print('')
        break
print('=-' * 30)
print('Z4:', end = ' ')
while True:
    print(times[cont3], end=', ')
    cont3 += 1
    if cont3 > 19:
        print('')
        break
print('=-' * 30)
print('Ordem álfabetica:', end = ' ')
while True:
    if times[cont4] == 'Chapecoense':
        chape_posicao = cont4 + 1
        break
    cont4 += 1
times.sort()
while True:
    print(times[cont5], end=', ')
    cont5 += 1
    if cont5 == 19:
        print('')
        break
print('=-' * 30)
print(f'A Chapecoense ficou na posição {chape_posicao}')
