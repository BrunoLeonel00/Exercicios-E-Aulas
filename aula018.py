
teste = list()
teste.append('bRUNO')
teste.append(12)
galera = list()
galera.append(teste[:])
teste[0] = 'Jose'

teste[1] = 1
galera.append(teste[:])
print(galera)
print('----' * 33)
pessoas = [['bruno', 2], ['cletion', 22], ['ana', 55]]
print(pessoas[1][0])
print('---for')
for dado in pessoas:
    print(f'{dado[0]} tem {dado[1]} anos de idade')
print('=====' * 33)
galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
tormaior = totmenor = 0
for c in galera:
    if c[1] >= 21:
        print(f'{c[0]} é maior de idade')
        tormaior += 1
    else:
        print(f'{c[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmenor} pessoas menores de idade')
print(f'e temos {tormaior} pessoas maiores de idade')