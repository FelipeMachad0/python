maior_idade = m_sexo = f_idade20 = 0
while True:
    print('-'*20)
    idade = int(input('IDADE: '))
    while True:
        sexo = str(input('SEXO: [M/F] ')).upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
        print('Gênero inválido')
    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        m_sexo += 1
    if sexo == 'F' and idade < 20:
        f_idade20 += 1
    print('-'*20)
    while True:
        continuar = str(input('QUER CONTINUAR? [S/N] ')).upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
        print('Opção inválida')
    if continuar == 'N':
        break
print(f'Tem {maior_idade} maiores de idade')
print(f'Tem {m_sexo} homens')
print(f'Tem {f_idade20} mulheres com menos de 20 anos')
