# -- coding: utf-8 --
print ("Введите возраст")
age = int(input())
print ("Введите ваше имя")
name = (input())

if age > 0 and age < 75  and  (name != 'Иван'):
       print("Поздравляем, Вы поступили во ВГУИТ!")
elif age >= 16:
    x = 17 - age 
    print("Сначала нужно окончить школу! Вам осталось учится", x,"г.") 
          