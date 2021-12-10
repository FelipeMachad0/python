km = int(input('Digite sua velocidade atual: '))
if km > 80:
    multa = km - 80
    multa = multa * 7
    print('Você ultrapassou o limite de velocidade! O limite da pista é 80 km/h! O valor da multa é R${}!'.format(multa))
else: 
    print('Parabéns! Você está no limite de velocidade!')
