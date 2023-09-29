print('--- loja bruninho---')
preço = float(input('Qual o preço do produto? '))
print('''[ 1 ] Dinheiro cheque: 10% de desconto
[ 2 ] A vista no cartão: 5% de desconto
[ 3 ] Em até duas vezes no cartão: Preço normal
[ 4 ] Em 3x o mais no cartão: 20% de juros''')
op = int(input('Qual seu metodo de pagamento? '))
if op == 1:
    desconto = preço - (10 / 100 * preço)
    print(f'Seu produto que antes custava R$ {preço}, passou a custar R${desconto}')
elif op == 2:
    desconto = preço - (5 / 100 * preço)
    print(F'Seu produto que antes custrava R$ {preço}, passou a custrar R${desconto}')
elif op == 3:
    print(f'O preço do produto nao sera alterado. Você pagará duas parcelas de {preço / 2}')
elif op == 4:
    parcelas = int(input('Ira pagar em quantas parcelas? '))
    acrescimo = preço + (20 / 100 * preço)
    print(f'Seu produto tera um acrescimo de 20%, o valor final sera de {acrescimo}.Em {parcelas} de {acrescimo / parcelas}')