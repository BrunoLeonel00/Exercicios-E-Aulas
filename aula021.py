def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(0)
f2 = fatorial(12)
f3 = fatorial(5)
print(f'Os fatoria sao {f1}, {f2}, E {f3}')


print('--------')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num =int(input('Digite um numero'))
if par(num):
    print('é par')
else:
    prin('É impar')