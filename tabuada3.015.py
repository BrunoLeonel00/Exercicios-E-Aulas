while True:
    n = int(input('Digite um numero para ver sua tabuada: '))
    if n < 0:
        print('Numero invalido')
        break
    for c in range(1, 11):
        print(f'{n} x {c:^2} = {n*c}')
    op = str(input('Deseja continuar? ')).strip().upper()[0]
    if op == 'N':
        break
print('Fim do programa')
