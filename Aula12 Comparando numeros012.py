numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite mais um numero: '))
if numero1 > numero2:
    print(f'O Numero {numero1} é maior que o {numero2} ')
elif numero2 > numero1:
    print(f'O numero {numero2} é maior que o {numero1}')
else:
    print('Ambos os numeros tem a mesma quantidade')
