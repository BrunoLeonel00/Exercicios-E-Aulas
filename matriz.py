matriz = [[], [], []]
totpar = tot_3_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um numero para a posição [{l}, {c}]')))
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(F'[ {matriz[l][c]:^5}]', end=' ')
    print()
print('Os números pares são: ', end='')
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]
            print(f'{matriz[l][c]}', end='...')
print()
print(f'E a soma deles é {totpar}')
for l in range(0, 3):
    for c in range(2, 3):
        tot_3_coluna += matriz[l][c]
print(f'A soma de todos os valores da terceira coluna são {tot_3_coluna}')
matriz[1].sort()
print(f'O maior valor da segunda coluna é {matriz[1][-1]}')
