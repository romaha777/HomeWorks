#!usr/bin/python3

# -*- coding: utf-8 -*import

number=int(input("Введите число для таблицы умножения: "))
num_x=0 # Задаём изначальное число для таблицы умножения
for repeat in range (10):
    num_x+=1 # Увеличиваем изначальное число на 1 для умножения числа от 1 до 10
    multiply=number*num_x # Умножаем число введённое пользователем на 1-10
    print(number, "x", num_x, "=", multiply)