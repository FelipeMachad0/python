pessoa = {'nome':'', 'media': 0}
pessoa['nome'] = str(input('Qual o nome do aluno? '))
pessoa['media'] = float(input(f'Qual a média do {pessoa["nome"]}? '))
print(f'Nome do aluno é {pessoa["nome"]}')
print(f'A média é igual a {pessoa["media"]}')
if pessoa['media'] < 6:
    print('REPROVADO')
else:
    print('APROVADO')
