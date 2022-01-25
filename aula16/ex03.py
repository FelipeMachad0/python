import random
cont = 0
n_sort = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
print('os valores sorteados foram:', end = ' ')
while True:
    print(n_sort[cont], end = ' ')
    cont += 1
    if cont == 5:
        print()
        break
n_sort.sort()
print(f'O menor valor é {n_sort[0]} e o maior é {n_sort[4]}')