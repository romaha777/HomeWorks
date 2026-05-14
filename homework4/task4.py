#!usr/bin/python3

# -*- coding: utf-8 -*import

import random
hidden_number=random.randint(1, 100)
print("Я загадал число от 1 до 100. У вас 7 попыток его угадать.")
count=1
while count < 8:
    print("Попытка ", count, ".", sep="", end=" ")
    while True:
        try:
            number=int(input("Введите число: "))
            break
        except ValueError:
            print("Вы ввели нечисловое значение! Попробуйте ещё раз!")
    if number > hidden_number:
        print("Слишком большое!")
        count+=1
    elif number < hidden_number:
        print("Слишком маленькое!")
        count+=1
    else:
        print("Поздравляю! Вы угадали!")
        break
if count == 8:
    print("Вы проиграли! Загаданное число было:", hidden_number)