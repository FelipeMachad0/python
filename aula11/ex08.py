peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)
print('O valor do IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
