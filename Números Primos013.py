n = int(input('Digite um numero: '))
for c in range(1, n+1):
    print(c)
    if n % c == 0:
        print('PRIMO')
        print('=' * 2)
    else:
        print('NÃO É PRIMO')
        print('=' * 2)
