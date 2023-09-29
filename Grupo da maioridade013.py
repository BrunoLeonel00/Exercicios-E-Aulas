from datetime import date
maior = menor = valho = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    if c > valho:
        valho = idade
    else:
        if valho < idade:
            valho = idade
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print(F'{maior} pessoas sao maiores de idade')
print(f'{menor} pessoas sao menores de idade')
print(f'a pessoa mais velha tem {valho} anos ')


