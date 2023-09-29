ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 20)
print(f'{"No":<4}{"Nome":<4}{"MEDIA":>8}')
print('-' * 26)
for pos, i in enumerate(ficha):
    print(f'{pos:<4}{i[0]:<4}{i[2]:>8.1f}')
while True:
    print('-' * 35)
    op = int(input('Mostrar notas de qual aluno (999 para parar)? '))
    if op == 999:
        print('Finalizando.....')
        break
    if op <= len(ficha) - 1:
        print(f'As notas de {ficha[op][0]} sao {ficha[op][1]}')
print('Volte sempre')

