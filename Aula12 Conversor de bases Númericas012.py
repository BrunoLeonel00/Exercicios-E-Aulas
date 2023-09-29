
numero = int(input('Digite um numero: '))
print('''[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] Hexagonal''')
op = int(input('qual a sua escolha? '))
if op == 1:
    print(f'Seu numero convertido para binario é igual a {bin(numero)[2::]}')
elif op == 2:
    print(f'Seu numero convertido para Octal é igual a {oct(numero)[2::]}')
elif op == 3:
    print(f'Seu numero convertido para Hexagonal é igual a {hex(numero)[2::]}')
else:
    print('Opção invalida')
