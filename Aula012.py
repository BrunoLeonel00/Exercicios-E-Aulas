nome = str(input('Qual o seu nome? ')).strip().upper()
if nome == 'BRUNO':
    print(f'Tenha um bom dia {nome}')
elif nome == 'JOSE' or nome == 'MARIA':
    print(f'Tenha um pessimo dia {nome}')
elif nome in 'ANA CLAUDIA JESSICA PEDRO':
    print('Feio')
else:
    print('Belo nome')
