from datetime import date
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: ')).strip()
trabalhador['Idade'] = int(input('Ano de nascimento: '))
trabalhador['Idade'] = date.today().year - trabalhador['Idade']
trabalhador['CTPS'] = int(input('Carteira de trabalho [ 0 se nao tiver]: '))
if trabalhador['CTPS'] == 0:
    print('-=' * 33)
    for p, dados in trabalhador.items():
        print(f'{p} tem valor {dados} ')
else:
    trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salario: '))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((35 +  trabalhador['Ano de contratação']) - date.today().year)
    print('-=' * 33)
    for p, dados in trabalhador.items():
        print(f'{p} tem valor {dados}')
