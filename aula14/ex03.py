from time import sleep
opcao = 4
while opcao != 5:
    if opcao == 1:
        resultado = num1 + num2
        print('=-' * 15)
        print('{} + {} = {}'.format(num1, num2, resultado))
        print('=-' * 15)
    elif opcao == 2:
        resultado = num1 * num2
        print('=-' * 15)
        print('{} x {} = {}'.format(num1, num2, resultado))
        print('=-' * 15)
    elif opcao == 3:
        if num1 > num2:
            resultado = num1    
        else:
            resultado = num2
        print('=-' * 15)
        print('entre {} e {} o maior é {}'.format(num1, num2, resultado))
        print('=-' * 15)
    elif opcao == 4:
        print('=-' * 15)
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))
        print('=-' * 15)
    else:
        print('=-' * 15)
        print('Opção invalida!')
        print('=-' * 15)
    sleep(0.5)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao = int(input('Escolha sua opção: '))
    sleep(0.5)
print('=-' * 15)
print('Obrigado por usar meu programa! ;)')
