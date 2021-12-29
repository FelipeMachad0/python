primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
    print('{} ➡️ '.format(primeiro_termo), end = " ")
    primeiro_termo += razao
print('FIM')
