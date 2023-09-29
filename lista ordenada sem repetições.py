lista_numeros = list()
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > lista_numeros[-1]:
        lista_numeros.append(n)
    else:
        pos = 0
        while pos < len(lista_numeros):  # Criei a variavel POS para conseguir varrer o vetor inteiro, e assim, descobrir as posições dos numeros, com a ajdua do len
            if n <= lista_numeros[pos]:  # verifiquei se o n é menor ou igual ao numero na lista, para colocar ele em uma posição especifica
                lista_numeros.insert(pos, n)
                break
            pos += 1 # para ir passando de posição
print('---' * 30)
print(f'Os numeros na lista são: {lista_numeros}')
