n = 1
soma = cont = 0
while n != 0:
    n = int(input('Digite um valor[0 para parar]: '))
    soma += n
    cont += 1
    if cont == 3:
        print('lindo')
        cont = 0
