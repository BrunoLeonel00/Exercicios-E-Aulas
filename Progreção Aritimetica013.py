pa = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
for c in range(0, 10):
    print(f'{pa} -> ', end=' ')
    pa += razao
print('ACABOU')
