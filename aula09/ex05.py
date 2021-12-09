frase = str(input('Digite uma frase: ')).lower().strip()
letra = str(input('Digite uma letra: ')).lower().strip()
quant = frase.count(letra)
primeiro = frase.find(letra) + 1
ultimo = frase.rfind(letra) + 1
print('a quantide de {} na frase é: {}'.format(letra, quant))
print('o primeiro {} aparece na posição: {}'.format(letra, primeiro))
print('o ultimo {} aparece na posição: {}'.format(letra, ultimo))
