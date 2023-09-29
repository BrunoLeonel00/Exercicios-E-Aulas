'''def area(a, l):
    print(f'Sua altura é {a} e a sua largura é {l}')
    areat = a * l
    print(f'Sua area é {areat}')


area(a=float(input('Largura (m): ')), l=float(input('Comprimento: ')))'''


def area():
    while True:
        print('--- Controle de terrenos ---')
        l = float(input('Largura (m): '))
        c = float(input('Comprimento (m): '))
        a = l * c
        print(f'A area desse terreno é {a}')

        resp = str(input('Quer adicionar mais um terreno? '))
        if resp == 'N':
            break

# Programa Principal
'''while True:
    print('--- Controle de terrenos ---')
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    area(l, c)
    resp = str(input('Quer adicionar mais um terreno? '))
    if resp == 'N':
        break
'''
area()
