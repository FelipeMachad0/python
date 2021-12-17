salario = float(input('Digite seu sálario: R$'))
if salario > 1250:
    salario = salario*1.10
else:
    salario = salario*1.15
print('O seu sálario atual é: {:.2f}'.format(salario))
