#!usr/bin/python3

# -*- coding: utf-8 -*import

names=["аННА", "иВАН", "МАРИЯ", "петр", "еЛЕНА"]

# Создаем кортеж из гласных букв
vowels=("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я",
"А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я")
FormattedNames=[] # Создаём новый список, в который будем помещать форматированные имена
for name in names: # Проходим по всем именам списка
    FormattedName=name.lower().capitalize() # Приводим имя к нижнему регистру и делаем первую букву заглавной
    if FormattedName.startswith(vowels): # Проверяем начинается ли имя на гласную
        FormattedName+="-STAR" # Если да, то добавляем суффикс
    FormattedNames.append(FormattedName) # Добавляем форматированное имя в новый список
print(f"{FormattedNames}")