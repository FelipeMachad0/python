#input para pegar valor da variavel
valor = input('digite algo: ')
#variaveis gerais
tipo = type(valor)
espaco = valor.isspace()
numero = valor.isnumeric()
alfabetico = valor.isalpha()
alfanumerico = valor.isalnum()
maiscula = valor.isupper()
minuscula = valor.islower()
maiscula_e_minuscula = valor.istitle()
#transformar valor true e false em verdadeiro e falso
if espaco == True: 
    espaco = 'verdadeiro'
else:
    espaco = 'falso'
if numero == True: 
    numero = 'verdadeiro'
else:
    numero = 'falso'
if alfabetico == True: 
    alfabetico = 'verdadeiro'
else:
    alfabetico = 'falso'
if alfanumerico == True: 
    alfanumerico = 'verdadeiro'
else:
    alfanumerico = 'falso'
if maiscula == True: 
    maiscula = 'verdadeiro'
else:
    maiscula = 'falso'
if minuscula == True: 
    minuscula = 'verdadeiro'
else:
    minuscula = 'falso'
if maiscula_e_minuscula == True: 
    maiscula_e_minuscula = 'verdadeiro'
else:
    maiscula_e_minuscula = 'falso'
#mostrar resultados na tela
print('O tipo primitivo desse valor é: {}'.format(tipo))
print('Só tem espaços? {}'.format(espaco))
print('É formado apenas por números? {}'.format(numero))
print('É formado apenas por letras? {}'.format(alfabetico))
print('É formado apenas por letras ou números? {}'.format(alfanumerico))
print('Está somente em maiusculas? {}'.format(maiscula))
print('Está somente em minusculas? {}'.format(minuscula))
print('Está em maiusculas e minusculas? {}'.format(maiscula_e_minuscula))