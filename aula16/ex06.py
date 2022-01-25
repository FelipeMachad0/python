palavras = []
while True:
    palavras.append(str(input('Digite um produto: ')).upper())
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
for p in palavras:
    print(f'Na palavra {p} temos as vogais: ', end = '')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end = ' ')
    print()
