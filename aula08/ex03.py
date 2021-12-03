n = float(input('digite um número: '))
print('O número na sua versão sem casas decimais é: {:.0f}'.format(n))
print('o número com casas decimais: {}'.format(n))

#fazendo com import
import math
n_int = math.trunc(n)
print('O número na sua versão sem casas decimais é: {}'.format(n_int))
print('o número com casas decimais: {}'.format(n))