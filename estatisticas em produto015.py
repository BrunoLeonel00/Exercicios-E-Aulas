total_gasto = produtos_mais_de_mil = cont = 0
produto_mais_barato = ' '
preco_barato = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total_gasto += preco
    cont += 1
    if preco > 1000:
        produtos_mais_de_mil += 1
    if cont == 1:
        produto_mais_barato = produto
        preco_barato = preco
    else:
        if preco_barato > preco:
            produto_mais_barato = produto
            preco_barato = preco
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'O total gasto na compra é {total_gasto}')
print(f'No carrinho estao {produtos_mais_de_mil} produtos acima de mill reais')
print(f'e o produto mais barato custa {preco_barato} e é {produto_mais_barato}')