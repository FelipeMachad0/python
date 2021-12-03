from math import radians, sin, cos, tan
angulo = float(input('digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('o valor do seno é: {:.2f}'.format(seno))
print('o valor do cosseno é: {:.2f}'.format(cosseno))
print('o valor da tangente é: {:.2f}'.format(tangente))
