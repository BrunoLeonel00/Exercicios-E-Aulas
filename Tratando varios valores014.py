n = 0
soma = cont = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n != 999:
        soma += n
        cont += 1
print(f'A soma dos {cont} numeros foi {soma}')
