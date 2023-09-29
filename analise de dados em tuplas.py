n = (int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numeroo: ')))
print(n)
print(f'O valor 9 apareceu {n.count(9) } vezes')
if 3 in n:
    print(f'O numero 3 está na posição {n.index(3) + 1}')
else:
    print('O valor 3 nao foi digitado ')
print('OS numeros pares sao:', end=' ')
for num in n:
    if num % 2 ==0:
        print(n)