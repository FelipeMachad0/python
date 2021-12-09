nome = str(input('Digite seu nome: ')).strip()
nome2 = nome.split()
print('seu primeiro nome é: {}'.format(nome2[0]))
print('seu último nome é: {}'.format(nome2[len(nome2) - 1]))
