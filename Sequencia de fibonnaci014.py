n = int(input('Quantos termos quer mostrar ?'))
t1 = 0  # por padrão a sequencia de fibonnaci começa com 0 e 1, ent ja preencho essas variaveis com eles
t2 = 1
cont = 3  # o contador começa com 3, porque ja temos dois termos(0 e 1)
print(f'{t1} -> {t2}  ', end='')
while cont <= n:
    t3 = t1 + t2  # a soma dos 2 antecessores nos da a continuação da sequencia
    print(f' -> {t3} ', end='')
    t1 = t2   # t1 ocupa o lugar do t2 para a sequencia continuar
    t2 = t3    # t2 vira t3 pelo mesmo motivo
    cont += 1
print(' -> Acabouu')