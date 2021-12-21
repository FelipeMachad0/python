#declaração de variaveis e importação de biblioteca
import datetime
ano = int(input('Que ano você nasceu? '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano
ano_faltam_alistamento = 18 - idade
ano_alistamento = ano + 18
#mostra o resultado na tela
print('Quem nasceu em {} tem {} anos'.format(ano, idade))
if ano_faltam_alistamento < 0:
    print('você se alistou a {} anos'.format(ano_faltam_alistamento * -1))
    print('você se alistou no ano de {}'.format(ano_alistamento))
elif ano_faltam_alistamento > 0:
    print('você vai se alistar daqui {} anos'.format(ano_faltam_alistamento))
    print('você vai se alistar no ano de {}'.format(ano_alistamento))
else:
    print('Você tem 18 anos, você se alista nesse ano')
