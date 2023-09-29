jogador =  dict()
partidas = list()
jogadores = list()
while True:
    jogador['Nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partidas {c}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    jogadores.append(jogador.copy())
    partidas.clear()
    while True:
        resp = str(input('Deseja continuar? ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=' * 33)
print(jogadores)
print(f'{"cod Nome"} {"Gols":>12} {"total":>14}')
for k, v in enumerate(jogadores):
    print(f'{k}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 30)
while True:
    busca = int(input('Qual jogador deseja buscar (999 para parar): '))
    if busca == 999:
        break
    if busca > len(jogadores):
        print('Nao existe esse jogador')
    else:
        print(f' ----- Levantamento do {jogadores[busca]["Nome"]}')
        for i, v in enumerate(jogadores[busca]['Gols']):
            print(f'    No jogo {i+1} fez {v} gols')