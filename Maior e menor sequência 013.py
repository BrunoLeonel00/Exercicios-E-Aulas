menor = maior = 0
for c in range(1, 6):
        peso = float(input('Peso: '))
        if c == 1:
            maior = peso
            menor = peso
        else:
            if maior < peso:
                maior = peso
            if menor > peso:
                menor = peso
print(f'O maior peso é {maior}kg')
print(f'e o menor peso é {menor}kg')
