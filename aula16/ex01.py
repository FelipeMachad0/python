while True:
    num_extensos = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
    while True:
        num_escolhido = int(input('Digite um número entre 0 e 10: '))
        if num_escolhido <= 10 and num_escolhido >= 0:
            break
        print('Número inválido')
    print(f'Você digitou o número {num_extensos[num_escolhido]}')
    s_n = str(input('Quer continuar? ')).upper()[0]
    if s_n == 'N':
        break
print('Obrigado por utilizar meu programa')
