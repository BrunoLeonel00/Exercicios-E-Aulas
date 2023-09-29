aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
for k, v in aluno.items():
    print(f'{k} é igual a {v} ')
if aluno['Media'] < 5:
    print('E esta´reprovado')
else:
    print('E está aprovado')
