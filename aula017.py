num = [1, 2, 3, 40, 7]
num.append(10) #adiciona um numero no final da lista
num.sort() # deixa organizado
num.sort(reverse=True) #deixa em ordem decresscente
len(num) #mostra os elemntos
num.insert(2, 2) #adicona um elemento na lista em qualquer posição
num.pop() # remove o ultimo valor, se nao quiser deletar o ultimo número indique entre os parentesses a posição do elemento que quer remover

print(num)
valores = list()
for c in range(0, 3):
    valores.append(int(input('Digite um numero: ')))
print('---------')
for v in valores:
    print(v, end=' ')
print('\n-------')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
print('-'*20)
a = [1, 2, 3, 4]
b = a
b.append(1)
print(f'Lista {a}')
print(f'lista {b}')
# A partir do momento que eu igualo uma lista com outra, quando eu mexo em uma eu mexo nas duas( PYthon cria uma ligação)
print('------')
b = a[:] # para nao criar essa ligação, nos criamos uma copia.