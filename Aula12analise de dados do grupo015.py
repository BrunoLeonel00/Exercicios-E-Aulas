mais_de_18anos = Homens_cadastrados = mulheres_menos_20anos = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade > 18:
        mais_de_18anos += 1
    if sexo == 'M':
        Homens_cadastrados += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres_menos_20anos += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar cadastradno pessoas? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'No grupo tem {mais_de_18anos} pessoas acima dos 18 anos')
print(f'Tem {Homens_cadastrados} Homens cadastrados')
print(f'E {mulheres_menos_20anos} mulheres com menos de 20 anos')
