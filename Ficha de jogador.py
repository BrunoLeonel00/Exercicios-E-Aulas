def jogador(nome='', gols=0):
    if nome == '':
        nome = 'Desconhecido'
    print(f'o Jogador {nome}, fez {gols} gols no campeonato')


craque = str(input('Nome do jogador: '))
gol = str(input('Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
jogador(craque, gol)
