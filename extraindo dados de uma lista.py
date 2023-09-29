lista = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    op = str(input('Deseja continuar? ')).strip().upper()
    if op == 'N':
        break
print(f'Foram digitados voce digitou {len(lista)} numeros ')
lista.sort(reverse=True)
print(f'A sua lista em decrescente é {lista}')
if 5 in lista:
    print('O valor 5 se encontra na lista')
else:
    print('5 nao esta na lista')
