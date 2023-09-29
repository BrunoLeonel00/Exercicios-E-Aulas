
lanche = ('Hamburgue', 'Suco', 'pudim', 'Pizza')
print(lanche[::-1])
print(sorted(lanche))  # organiza a tupla, lista, dic....
print('-------------')
# qunado somamos uma tupla com outra, elas se juntam e viram uma só.
a = 1, 2, 3
b = 2, 4, 5
c = a + b
print(c.count(3))
print(c.index(5))
del(c) # apaga uma tupla


print('--------------')
for c in range(0, len(lanche)):  #ajuda quando precisar mostrar a posição
    print(f'Eu comi {lanche[c]} na posição {c}')
print('---------')
for c in lanche:
    print(f'eu comi {c}')
print('-------')
for pos, c in enumerate(lanche):
    print(f'\n{c} {pos}')    # esssa tambem ajuda na posição

