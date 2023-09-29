r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo')
    if r1 == r2 == r3:
        print('Formam um triangulo equilatero')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Podem formar um  triangulo isóceles')
elif r1 != r2 != r3 != r1:
    print('Formam um triangulo escaleno ')
