from random import shuffle
aluno1 = input('digite o nome do 1º aluno/a: ')
aluno2 = input('digite o nome do 2º aluno/a: ')
aluno3 = input('digite o nome do 3º aluno/a: ')
aluno4 = input('digite o nome do 4º aluno/a: ')
array = [aluno1, aluno2, aluno3, aluno4]
shuffle(array)
print('a ordem dos alunos é: {}'.format(array))
