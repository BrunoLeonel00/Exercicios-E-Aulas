'''for c in range(0, 1):
    frase = str(input('Digite uma frase: ')).strip().upper()
    if ''.join(frase[::-1]) == ''.join(frase):
        print('É um palindromo')
junto = ''.join(frase[-1:-1:-1])
print(junto)
print(''.join(frase))'''

frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('É ium palindromo ')
