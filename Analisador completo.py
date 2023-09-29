soma = Hvelho = Menor20 = 0
velho = ' '
for c in range(1, 5):
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    print('-=' * 10)
    soma += idade
    media = soma / 4
    if sexo == 'M':
        if c == 1:
            Hvelho = idade
        else:
            if Hvelho < idade:
                Hvelho = idade
                velho = nome
    if sexo == 'F':
        if idade < 20:
            Menor20 += 1
print(f'a media do grupó é {media} ')
print(f'A idade do homem mais velho é {Hvelho} e seu nome é {velho}')
print(f'no grupo tem {Menor20} mulheres menores de 20 anos ')
