p_a = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
while cont < 10:
    print(f'{p_a} -> ', end='')
    p_a += razao
    cont += 1
print('FIM')