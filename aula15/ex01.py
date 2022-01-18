valor = n = soma = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 0:
        break
    valor += 1
    soma += n
print(f'A soma dos {valor} é igual a {soma}')
