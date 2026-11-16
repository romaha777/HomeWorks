#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Запрос имени файла
name_file = input("Введите имя файла (например, beer.txt): ")

# Запись 5 строк в файл
with open(name_file, "w") as file:
    print("Введите 5 строк для записи в файл:")
    file.write(input("Введите первую строку: ") + "\n")
    file.write(input("Введите вторую строку: ") + "\n")
    file.write(input("Введите третью строку: ") + "\n")
    file.write(input("Введите четвертую строку: ") + "\n")
    file.write(input("Введите пятую строку: "))

# Чтение содержимого файла
with open(name_file, "r") as file:
    content = file.read()
    print(content)