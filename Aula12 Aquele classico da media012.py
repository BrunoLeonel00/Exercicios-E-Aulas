print('===\033[1;34mCALCULANDO MEDIA\033[M')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Reprovado')
elif media <= 6.9:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')

