nota_geral = []
nota = []
cont = mostrar = 0
while True:
    nota.append(str(input('Insira nome do aluno: ')))
    nota.append(float(input('Insira a nota 1 do aluno: ')))
    nota.append(float(input('Insira a nota 2 do aluno: ')))
    nota.append((nota[1]+nota[2])/2)
    nota_geral.append(nota)
    nota = []
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('N. NOME       MÉDIA')
print('-'*20)
while cont < len(nota_geral):
    print(f'{cont:<3}{nota_geral[cont][0]:<9}{nota_geral[cont][3]:>8.1f}')
    cont += 1
while True:
    mostrar = int(input('Mostrar nomes de qual aluno (999 para interromper): '))
    if mostrar == 999:
        break
    print(f'As notas de {nota_geral[mostrar][0]} são {nota_geral[mostrar][1:3]}')
