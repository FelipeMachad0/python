l1 = float(input('qual o tamanho do lado 1: '))
l2 = float(input('qual o tamanho do lado 2: '))
l3 = float(input('qual o tamanho do lado 3: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('forma um triangulo')
else:
    print('não forma um triangulo')
    