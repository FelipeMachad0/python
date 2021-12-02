salario_atual = float(input('quanto o funcionario recebe atualmente? R$'))
aumento = float(input('quantos % de aumento ele vai receber? '))
aumento_calculo = aumento/100
salario_novo = salario_atual + salario_atual*aumento_calculo
print('O funcionario que recebia R${:.2f} com {:.0f}% de aumento vai receber R${:.2f}'.format(salario_atual, aumento, salario_novo))