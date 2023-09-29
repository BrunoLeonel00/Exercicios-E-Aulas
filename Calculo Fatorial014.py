n = int(input('Digite um numero para saner seu fatorial: '))
c = n
mult = 1
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    mult *= c
    c -= 1
print(f' {mult}')
