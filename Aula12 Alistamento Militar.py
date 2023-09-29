from datetime import date
print('====\033[1;36m Alistamento Militar\033[m ====')
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade < 18:
    print(f'Voce tem {idade} anos. E devera se alistar daqui a {18 - idade} anos ')
elif idade == 18:
    print(f'Vocês tem {idade} anos. E deve se alistar agora!')
elif idade > 18:
    print(f'Voce tem {idade} anos. E ja se passaram {idade - 18} anos do seu alistamento')

