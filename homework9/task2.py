#!/usr/bin/python3

# -*- coding: utf-8 -*-

try:
    # Открываем и читаем файл
    with open("data.txt", "r") as file:
        lines = file.readlines()

    # Преобразуем строки в числа (пропускаем пустые строки)
    numbers = []
    for line in lines:
        line = line.strip()
        if line:  # Пропускаем пустые строки
            numbers.append(float(line))

    # Вычисляем сумму и среднее арифметическое
    total = sum(numbers)
    average = total / len(numbers)

    # Записываем результат в новый файл
    with open("result.txt", "w") as result:
        result.write(f"Сумма чисел: {total}\n")
        result.write(f"Среднее арифметическое чисел: {average}")

except FileNotFoundError:
    print("Ошибка: файл data.txt не найден.")
except ValueError:
    print("Ошибка: в data.txt есть некорректные данные (не числа).")
except Exception as e:
    print(f"Другая ошибка: {e}")