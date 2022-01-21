cont = cont2 = cont3 = 0
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
    print(times[-cont3], end=', ')
    cont3 += 1
    if cont3 > 3:
        break
