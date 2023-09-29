n = 1
while n != 0:
    nome = str(input('Nome: ')).strip().upper()
    sexo = str(input('Sexo: '))
    while sexo not in 'MF':
        print('\033[1;31mSexo invalido\033[m')
        sexo = str(input('Sexo [M/F}: ')).upper()

    n = int(input('Digite 0 para PARAR: '))
