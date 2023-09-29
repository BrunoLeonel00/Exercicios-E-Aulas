numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezesete', 'dezoito', 'dezenove',
           'vinte',)
while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    while escolha < 0 or escolha > 20:
        escolha = int(input('Tente Novamnte. Digite um numero entre 0 e 20: '))
    print(f'Voce escolheu {numeros[escolha]}')
    op = ' '
    while op not in 'SN':
        op = str(input('Voce quer continuar? ')).strip().upper()[0]
    if op == 'N':
        break
print('Acabou')