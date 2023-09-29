dados_do_jogador = dict()
totaG = 0
dados_do_jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidar ele jogou? '))
lista_gols = list()
for c in range(1, partidas + 1):
    n = int(input(f'Quantos gols na {c} partida: '))
    totaG += n
    lista_gols.append(n)
    dados_do_jogador['Gols'] = lista_gols.copy()
dados_do_jogador['total'] = totaG
print('-=' * 33)
print(dados_do_jogador)
print('=-' * 33)
for k, v in dados_do_jogador.items():
    print(f'{k} tem valor {v}')
print('=-' * 33)
print(f'O jogador {dados_do_jogador["Nome"]} jogou {partidas} partidas')
for p, v in enumerate(lista_gols):
    print(f' => Na partida {p+1} fez {v} ')
print(f'Foi um total de {totaG} gols')
