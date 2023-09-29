n = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
op = 0
while op != 5:
    print('''[ 1 ] soma 
[ 2 ] Multiplicar
[ 3 ] maior 
[ 4 ] Novos números 
[ 5 ] sair do programa''')
    op = int(input('Qual a sua opção? '))
    if op == 1:
        print(f'A soma de ambos os numeros é {n + n2}')
    elif op == 2:
        print(f'A multiplicação de {n} e {n2} é {n * n2}')
    elif op == 3:
        if n > n2:
            print(f'O {n} é maior que {n2}')
        elif n < n2:
            print(f'o {n2} é maior que {n}')
        elif n == n2:
            print('ambos tem o mesmo valor')
    elif op == 4:
        n = int(input('Digite os novos numeros:'))
        n2 = int(input('Digite os novos numeros: '))
    print('-=' * 20)
print('Obrigado, volte sempre')

