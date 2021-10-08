def n(num):
    if num > 0:
        return 1
    else:
        return 0
try:
    num = int(input('введите число:'))
    sist = int(input('введите целевую систему счисления:'))
    while sist != 2 and sist != 8:
        print('нужно выбрать двоичную или восьмиричную систему счисления')
        sist = int(input())
    if sist == 2:
        b = ''
        while n(num) == 1:
            b = str(num % 2) + b
            num = num // 2
        print(b)
    if sist == 8:
        a = ''
        while n(num) == 1:
            a = str(num % 8) + a
            num = num // 8
        print(a)
except ValueError:
    print('это не число. введите число')