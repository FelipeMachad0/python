sexo = str(input('Informe seu gênero: [M/F] ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe um gênero válido: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))