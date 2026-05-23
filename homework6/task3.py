#!/usr/bin/python3

# -*- coding: utf-8 -*-

cities_data = [
    ("Москва", (55.7558, 37.6173), 12600000),
    ("Санкт-Петербург", (59.9343, 30.3351), 5400000),
    ("Казань", (55.7964, 49.1088), 1250000),
    ("Новосибирск", (55.0302, 82.9204), 1600000)
]

cities_info = {}
moscow_coord = cities_data[0][1] # Вычисляем координаты Москвы

for city, coord, population in cities_data: # Проходим по списку для вычисления дистанции до Москвы и создания нужного словаря
    x, y = coord
    dist_to_moscow = ((x - moscow_coord[0]) ** 2 + (y - moscow_coord[1]) ** 2) ** 0.5 # Вычисляем дистанцию до Москвы
    dist_to_moscow = round(dist_to_moscow, 2) # Округляем её до 2 знаков
    cities_info[city] = {                     # Добавляем необходимые данные в словарь
        "координаты": coord,
        "население": population,
        "расстояние_до_москвы": dist_to_moscow
    }

print(f"Словарь городов с расстояниями: {cities_info}")