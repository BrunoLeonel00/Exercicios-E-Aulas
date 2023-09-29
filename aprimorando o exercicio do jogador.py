dados_do_jogador = dict()
jogadores = list()
lista_gols = list()
gols_geral = list()
totaG = 0
while True:
    dados_do_jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidar ele jogou? '))
    for c in range(1, partidas + 1):
        n = int(input(f'Quantos gols na {c} partida: '))
        totaG += n

        lista_gols.append(n)
    dados_do_jogador['Gols'] = lista_gols[:]
    dados_do_jogador['total'] = totaG
    jogadores.append(dados_do_jogador.copy())
    lista_gols.clear()
    totaG = 0
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(jogadores)
print('-=' * 33)
print(f'{"Cod Nome":<4} {"Gols":>5} {"Total":>8}')
print('---' * 12)
for d in jogadores:
    for k, v in d.items():
        print(f'{v}', end=' ')
    print()
while True:
    while True:
        es = int(input('Deseja mostrar dados de qual jogador? '))
        if es <= len(jogadores):
            break
    print(f'Levantamento do jogador {d[es]}')
    if es == 999:
        break

