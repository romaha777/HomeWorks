#!usr/bin/python3

# -*- coding: utf-8 -*import

# Присваиваем нулевые значения суммам символов
SummLetter=0
SummNumber=0
SummSpace=0
AnotherSymbol=0
text=input("Введите текст:\n") # Просим пользователя ввести текст
for symbol in text: # Прогоняем каждый символ текста через цикл for
    if symbol.isalpha()==True: # Подсчитываем количество букв
        SummLetter+=1
    elif symbol.isdigit()==True: # Подсчитываем количество цифр
        SummNumber+=1
    elif symbol.isspace()==True: # Подсчитываем количество пробелов
        SummSpace+=1
    else: # Подсчитываем количество других символов
        AnotherSymbol+=1
print(f"""Буквы: {SummLetter}
Цифры: {SummNumber}
Пробелы: {SummSpace}
Прочие: {AnotherSymbol}""")