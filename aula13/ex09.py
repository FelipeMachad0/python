import datetime
maior = 0
menor = 0
ano_atual = datetime.date.today().year
for c in range(1,8):
    ano_nasc = int(input('Em qual ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano_atual - ano_nasc
    if idade < 0 or idade > 120:
        print('ERRO! Ano de nascimento inválido, tente novamente!')
    else:
        if idade >= 18:
            maior += 1
        else:
            menor += 1
print('São {} maiores de idade e {} menores de idade'.format(maior, menor))
