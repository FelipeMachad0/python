tabuada = int(input("insira um número pra ver sua tabuada: "))
print('-=' * 12)
for c in range(1,11):
    valor = tabuada*c
    print('{} x  {} = {}'.format(tabuada, c, valor))
print('-=' * 12)
