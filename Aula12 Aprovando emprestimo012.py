print('---\033[1;35mBanco\033[m---')

Casa = float(input('Qual o valor da residencia? '))
Salario = float(input('Salario do comprador: '))
anos = int(input('Em quantos anos voce ira pagar a casa? '))
limite = 30 / 100 * Salario
prestacao = Casa / (anos * 12)
print(f'Voce tera que pagar uma casa de R${Casa} ao longo de {anos} Anos. Sua prestação sera de {prestacao:.2f}')
if prestacao > limite:
    print('Emprestimo Negado')
elif prestacao <= limite:
    print('Emprestimo Aceito')
