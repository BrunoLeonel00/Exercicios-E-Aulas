pessoa = dict()
galera = list()
meida = list()
mulher = list()
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    galera.append(pessoa.copy())
    meida.append(pessoa['Idade'])
    if pessoa['Sexo'] == 'F':
        mulher.append(pessoa['Nome'])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break
    print('-=' * 20)
print(f'No total foram {len(galera)} pessoas cadastradas')
media = 0
for i in meida:
    media += i
media /= len(galera)
print()
print(f'A idade media de idade do grupo é {media:.2f}')
for c in galera:
    for i, v in c.items():
        if i == 'Sexo' and v == 'F':
            print(f'As mulheres do grupo sao: {mulher}')
print()
print(F'As pessoas acima da media sao: ')
for c in galera:
    for p, i in c.items():
        if p == 'Idade' and i > media:
            print(f'{c["Nome"]}, com {i} anos') 
