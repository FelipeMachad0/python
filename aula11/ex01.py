valor_casa = float(input('Qual o valor da casa que você quer comprar? R$'))
sal = float(input('Digite seu sálario: R$'))
tempo = float(input('Em quantos anos você vai pagar a casa? '))
prestacao = sal*0.3
prestacao_mensal = valor_casa/(tempo*12)
if prestacao < prestacao_mensal:
    print('Você não pode pagar a prestação da casa')
else:
    print('O valor da prestação foi aceito')
