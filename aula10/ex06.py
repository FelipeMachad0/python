array = [1, 2, 3]
array[0] = int(input('digite um número: '))
array[1] = int(input('digite outro número: '))
array[2] = int(input('digite outro número: '))
array.sort()
print('O número mais baixo é: {}\nO número mais alto é: {}'.format(array[0], array[2]))
