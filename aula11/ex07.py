l1 = float(input('qual o tamanho do lado 1: '))
l2 = float(input('qual o tamanho do lado 2: '))
l3 = float(input('qual o tamanho do lado 3: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3:
        print('forma um triangulo equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('forma um triangulo isóceles')
    else:
        print('forma um triangulo escaleno')
else:
    print('não forma um triangulo')
