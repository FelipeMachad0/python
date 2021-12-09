nome = str(input('Digite seu nome completo: ')).strip()
comparar = str(input('Digite qual nome você quer saber se tem: ')).strip().lower()
nome02 = comparar in nome.lower()
if nome02 == True:
    print('Seu nome tem {}'.format(comparar.capitalize()))
else:
    print('Seu nome não tem {}'.format(comparar.capitalize()))
