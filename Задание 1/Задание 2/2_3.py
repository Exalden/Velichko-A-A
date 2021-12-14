# -- coding: utf-8 --
print('Введите число минут')
n=int(input())
n=n%(24*60)
a=n%60
b=n//60
print(b,'часов',a, 'минут')