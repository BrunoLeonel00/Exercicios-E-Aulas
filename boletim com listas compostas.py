lista_alunos = list()
nota = list()
geral = list()
cont = 0
while True:
    lista_alunos.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota2: ')))
    lista_alunos.append(nota[:])
    geral.append(lista_alunos[:])
    lista_alunos.clear()
    nota.clear()
    resp = str(input('Deseja continuar? ')).strip().upper()
    if resp == 'N':
        break
print(geral)
print('-=' * 30)
print(F'No. {"Nome":>2} {"MEDIA":>8}')
print('-' * 20)
media = 0
for pos, i in enumerate(geral):
    print(f'{pos:>2}  {i[0]} ', end='')
    for n in geral[pos][1]:
        media = n + n
    print(f'{media / 2:> 8}')
    media = 0
print('-=' * 20)
while True:
    op = int(input('Mostrar Nostas de qual aluno (999 para parar): '))
    if op == 999:
        break
    if op <= len(geral) - 1:
        print(f'Notas de {geral[op][0]}  sao {geral[op][1]}')
    print('-=' * 20)
print('Volte sempre')
