pessoas = list()
dados = list()
cont = maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')).strip())
    peso = float(input('peso: Kg '))
    cont += 1
    if cont == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    pessoas.append(peso)
    dados.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-' * 33)
print(f'Ao todo foram cadastradas {len(dados)} pessoas.')
print(f'O maior peso é {maior}.Que são. ', end='')
for pos, i in enumerate(dados):
    if dados[pos][1] == maior:
        print(f'{dados[pos][0]}...', end=' ')
print()
print(f'E o menor peso é {menor}Kg. Que são', end='')
for pos, i in enumerate(dados):
    if dados[pos][1] == menor:
        print(f' {dados[pos][0]}', end=' ')
print()
