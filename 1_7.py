# -- coding: utf-8 --
print("Введите число")
number = int(input())
if number%2 == 0:
  print('Число', number,'чётное')
elif number%2 != 0: print('Число', number,'не чётное')