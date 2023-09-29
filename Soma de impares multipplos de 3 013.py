s = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A soma de todos os numeros multiplos de 3 é {s}, e foram {cont} numeros')
