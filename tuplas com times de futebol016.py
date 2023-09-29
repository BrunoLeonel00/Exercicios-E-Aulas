time = ('Botafogo', 'Santos', 'Fluminense', 'Chapecoense', 'corinthians',
        'São paulo', 'Flamengo', 'Palmeiras', 'Gremio', 'Bragantino',
        'Athletico', 'Fortalza', 'CUIABA', 'Bahia', 'Goias', 'Santos',
        'vasco', 'america', 'Minas', 'coritiba',)
print(f'Os cinco primeiros sao {time[:5]}')
print('------')
print(f'Os ultimos quatro sao {time[-4:]}')
print('------')
print(f'Os times em ordem alfabeticam sao: {sorted(time)}')
print('------')
print(f'A chapecoense esta na posicao {time.index("Chapecoense")}')