nota1 = float(input('escreva sua nota 1: '))
nota2 = float(input('escreva sua nota 2: '))
media = (nota1 + nota2)/2
if media < 5:
    print('reprovado')
elif media < 7:
    print('recuperação')
else:
    print('aprovado')
