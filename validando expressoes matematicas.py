expressao = str(input('Digite a expressao: '))
pilha = []
for sim in expressao:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão valida')
else:
    print('Expressao invalida')
