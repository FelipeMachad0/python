primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
whiles = 10
while whiles > 0:
    print('{} ➡️ '.format(primeiro_termo), end = " ")
    primeiro_termo += razao
    if whiles > 1:
        whiles -= 1
    else:
        print('FIM')
        whiles = int(input('Quantas vezes mais você quer fazer? '))
print('Obrigado por utilizar meu programa')
