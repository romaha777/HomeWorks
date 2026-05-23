#!/usr/bin/python3

# -*- coding: utf-8 -*-

students_data = [
    ("Анна", 101, [4, 5, 4]),
    ("Борис", 102, [3, 4, 3]),
    ("Виктор", 101, [5, 5, 4]),
    ("Галина", 102, [4, 4, 5])
]
group_dict = {}
name_dict = {}

# Создаю словарь, где ключ - номер группы,
# а значения - списики имен этой группы

for name, group, assessments in students_data:
    if group not in group_dict:
        group_dict[group] = []
    group_dict[group].append(name)

# Создаю новый словарь, где ключ - имя студента,
# а значение - средний балл

for name, group, assessments in students_data:
        average_assessment = 0
        count = 0
        for assessment in assessments:
            average_assessment += assessment
            count += 1
            average_score = round(average_assessment / count, 2)
        if name not in name_dict:
            name_dict.update({name: average_score})   

# Вывожу студентов с их средним баллом по группам

for group, names in group_dict.items():
    print(f"Группа {group}:")
    for name in names:
        print(f"- {name}: средний балл {name_dict[name]}")

    # Вывожу студента с наивысшим средним баллом в каждой группе

    best_student = max(names, key=lambda n: name_dict[n])
    print(f"Студент с наивысшим баллом: {best_student} ({name_dict[best_student]})")