p1 = p2 = 0
expressao = str(input('Digite a expressão: '))
for c in expressao:
    if c == '(':
        p1 += 1
    elif c == ')':
        p2 += 1
if p1 == p2:
    print('expressão válida')
else:
    print('expressão inválida')
