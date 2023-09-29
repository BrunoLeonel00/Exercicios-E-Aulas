def fatorial(num=0, show=False):
    """
    Calcula o Fatorial de cada numeros
    :param num: o numero a ser calculado
    :param show: (opcional) para mostrar o desenorlar da conta
    :return: rentorna o resultado
    """
    f = 1
    if show:
        for c in range(num, 0, -1):
            f *= c
            print(f'{c} ', end='x')
    else:
        for c in range(num, 0, -1):
            f *= c
    return f


print(fatorial(5))
