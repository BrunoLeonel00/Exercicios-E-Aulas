def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mDigite um numero\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leia_int('Digite um numero: ')
print(f'Voce digitou o numero {n}')
