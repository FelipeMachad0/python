import datetime
ano_nasc = int(input('digite o ano que você nasceu: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
if 9 >= idade:
    print('mirim')
elif 14 >= idade:
    print('infantil')
elif 19 >= idade:
    print('junior')
elif 25>= idade:
    print('sênior')
else: 
    print('master')
