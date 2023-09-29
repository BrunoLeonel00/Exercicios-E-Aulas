from time import sleep


def maior(*num):
    total = len(num)
    print('-=' * 20)
    print('Analisando os valores....')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
    print(f' Foram informados {total} valores ')
    if not num:
        print('O maior valor é 0')
    else:
        print(f'o maior deles é {max(num)}')


maior(1, 3, 4, 5, 6, 5)
maior(0)
maior()
