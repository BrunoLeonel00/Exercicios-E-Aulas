lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite varios numeros'))
    lista.append(n)
    resp = str(input('deseja continuar? ')).upper()

    if resp == 'N':
        break
print('A lista completa é')
for pos, c in enumerate(lista):
    print(f' {c}', end=' ')
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'\nEssa é a lista com pares {par}')
print(f'Essa é a lsita com impares {impar}')
