'''ef main():
    # Comandos da função
    pass


main()'''
'''meu_nome = 'Bruno'


def dados():
    nome = str(input('Digite seu nome: '))
    idade = int(input('Idade'))
    sexo = str(input('Sexo '))
    print(f'Ola {nome} você tem {idade} anos e é do sexo {sexo}.')


print('------' * 33)


def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


minha_media = media(10, 10)
print(minha_media)

print('----' * 30)


def media():
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    return media


minha_media = media()
print(minha_media)

print('------')

dados()
media()''''''



'''

'''def media():
    nota1 = float(input('noTA: '))
    nota2 = float(input('Nota: '))
    return calcular_media(nota1, nota1)


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


minha_media = media()
print('Minha media é: ', minha_media)'''

'''def media():
    nota1 = float(input('Nota '))
    nota2 = float(input('Nota2  '))
    return minha_media(nota1, nota2)


def minha_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


def situaçao(media):
    if (media > 6):
        print('Aprovado')
    else:
        print('Reprovado')


situaçao(media())'''


def lin():
    print('-' * 20)



def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f' A soma de {a} mais {b} é {s}')


# programa principal
soma(4, 1)
#FIM
lin()


def contador(*num):
    tam = len(num)
    print(f'A os numeros sao {num} e o todo tem {tam}')


contador(1, 2, 3, 4, 5,)
# fim
lin()


def dobra(lts):
    pos = 0
    while pos < len(lts):
        lts[pos] *= 2
        pos += 1
    print(lts)


valores = [1, 3, 4, 3, 2, 1]
dobra(valores)

