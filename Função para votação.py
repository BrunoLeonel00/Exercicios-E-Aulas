
def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Voce tem {idade} anos, e o voto esta NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'VOCE tem {idade} amos Voto opcional'
    else:
        return f'Voto Obrigadtorio'


nascimento = int(input('Em que ano voce nasceu? '))
print(voto(nascimento))
