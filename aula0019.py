'''pessoas = {'nome': 'Gustavo', 'idade': 12}
          #KEYS     VALUES
            # E PARA MOSTRAR TUDO : ITEMS
del pessoas[# Key que quer excluir]
pessoas['nome'] = 'Bruno'
pessoas['Sexo'] = 'm'
for k, v in pessoas.items():  #Funciona igual o enumerate (Mas tem q usar o comando Items
    print(F'{k} = {v}')


print('----------')
for v in pessoas.values(): #Mostra todos os valores do dicionarios
    print(f'{v}'''
brasil = list()
estado = dict()
for c in range(0, 2):
    estado['Uf'] = str(input('Digite o UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
    estado.clear()
print('---------')
print(brasil)
for e in brasil:
    for v in e.values():
        print(f'{v} ', end='= ')
    print()