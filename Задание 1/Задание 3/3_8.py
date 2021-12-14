# -- coding: utf-8 --
def S():
    n = int(input("Введите число от 1 до 9"))
    if 1 <= n <= 9:
        for i in range(1, n + 1):
            for a in range(1, i + 1):
                print(a, sep='', end='')
            print()

print(S())