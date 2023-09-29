par = list()
impar = list()
completa = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c} numero: '))
    if n % 2 == 0:
        completa[0].append(n)
    elif n % 2 == 1:
        impar.append(n)
        completa[1].append(n)
print('-' * 30)
print(completa)
completa[0].sort()
print(f'A lista de numeros pares: {completa[0]}')
print()
completa[1].sort()
print(f'A lista de numeros impares; {completa[1]}')
