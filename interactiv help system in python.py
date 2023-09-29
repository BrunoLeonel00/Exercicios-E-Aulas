from time import sleep


def h(ajuda):
    print('Sistema de ajuda')
    ok = False
    while True:
        op = str(input(ajuda))
        ok = True
        if op == 'fim':
            break
        print('\033[1;34m')
        help(op)
        print('\033[m')
    sleep(1)
    return op


op = h('Função ou biblioteca: ')

print(f'\033[1;34m{op}\033[m')
