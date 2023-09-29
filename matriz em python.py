matriz = [[], [], []]
for c in range(0, 3):
    for x in range(0, 3):  # enqunato esse for trabalha(dando os valores de 0,1,2. O for de cima se mantem no valor do laço inicial, ate o segundo for completar o laço
        matriz[c].append(int(input(f'Digite um numero [{c}, {x}]: ')))
for c in range(0, 3):
    for x in range(0, 3): # a mesma ideia,
        print(f'[{matriz[c][x]}]', end=' ')
        print()
