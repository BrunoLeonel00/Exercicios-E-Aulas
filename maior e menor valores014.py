s = ' '
maior = menor = totnumeros = cont = 0
while s not in 'N':
    n = int(input('Digite um numero: '))
    cont += n
    totnumeros += 1
    media = cont / totnumeros
    if totnumeros == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    s = str(input('Deseja continuar? ')).upper()[0]
print(f' a media dos numeros digitados é {media}')
print(f' o maior numero é {maior} e o menor é {menor }')
