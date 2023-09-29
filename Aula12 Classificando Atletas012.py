from datetime import date
nascimento = int(input('Ano de nascimento do atleta: '))
categoria = date.today().year - nascimento
if categoria <= 9:
    print('Analisando sua idade. A sua categoria será MIRIM')
elif categoria <= 14:
    print('Analisando a sua idade. Sua categoria será INFANTIL')
elif categoria <= 19:
    print('Analisando a sua idade. Sua categoria sera JUNIOR')
elif categoria == 25:
    print('Analisando a sua idade. Sua categoria será SENIOR')
else:
    print('Analsinado a sua idade. Sua categoria será MASTER')
