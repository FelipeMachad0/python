resultado = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        resultado += num
print('A soma dos valores pares da: {}'.format(resultado))
