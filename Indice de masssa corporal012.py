peso = float(input('peso: '))
altura = float(input('Altura: '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.2f}. Esta abaixo de peso')
elif IMC <= 25:
    print(f'Seu IMC é de {IMC:.2F}. Esta no peso ideal')
elif IMC <= 30:
    print(f'Seu IMC é de {IMC:.2F}. Esta com sobrepeso')
elif IMC <= 40:
    print(f'Seu IMC é de {IMC:.2F}. Esta com obesidade')
elif IMC > 40:
    print(f'Seu IMC é de {IMC:.2F}. Esta com obesidade morbida. PERIGO!!!')
