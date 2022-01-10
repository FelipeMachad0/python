#declaração variaveis
idade_med = 0
idade_maior = -1
quant_menor = 0
#laço for para pegar os dados
for c in range(1, 5):
    print('-----{}ª pessoa-----'.format(c))
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    genero = str(input('Gênero [M/F]: ')).upper()
    #calcular média de idade
    idade_med += idade
    #calcular homem mais velho
    if idade > idade_maior and genero == 'M':
        idade_maior = idade
        homem_velho = nome.capitalize()
    #calcular número de mulheres menores de idade
    if idade < 18 and genero == 'F':
        quant_menor += 1
idade_med = idade_med / 4
#mostrar resultados na tela
print('A média de idade é {}'.format(idade_med))
print('O homem mais velho tem {} anos e se chama {}'.format(idade_maior, homem_velho))
print('Tem {} mulheres menores de idade'.format(quant_menor))
