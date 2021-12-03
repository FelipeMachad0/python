cat_oposto = float(input('digite o valor do cateto oposto: '))
cat_adjacente = float(input('digite o valor do cateto adjacente: '))
hipotenusa = cat_adjacente**2 + cat_oposto**2
hipotenusa = hipotenusa**(1/2)
print('o valor da hipotenusa é: {:.2f}'.format(hipotenusa))

#com import
import math
hipotenusa_math = math.hypot(cat_oposto, cat_adjacente)
print('o valor da hipotenusa é: {:.2f}'.format(hipotenusa_math))
