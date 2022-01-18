while True:
    tabuada = int(input("insira um número pra ver sua tabuada: "))
    print('-=' * 25)
    c = 0
    if tabuada < 0:
        break
    while True:
        if c > 10:
            break
        valor = tabuada*c
        print(f'{tabuada} x  {c} = {valor}')
        c += 1
    print('-=' * 25)
print('Muito obrigado por utilizar meu programa!!')
