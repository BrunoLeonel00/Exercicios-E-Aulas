produtoos = ('pao', 12, 'caderno', 2, 'coelho', 2)
for pos, i in enumerate(produtoos):
    if pos % 2 == 0:
        print(f'{produtoos[pos]:.<20}',end='R$ ')
    else:
        print(f'{produtoos[pos]:.2f}')