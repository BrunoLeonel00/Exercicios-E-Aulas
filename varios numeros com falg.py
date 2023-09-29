soma = contador = 0
while True:
    n = int(input('Digite um numeros(Digite 999 para parar): '))
    if n == 999:
        break
    soma += n
    contador += 1
print(F'A soma de todos os {contador } numeros digitados é {soma}')