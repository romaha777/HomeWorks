#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Импорт всего модуля

import converter
print(converter.celsius_to_fahrenheit(5))
print(converter.fahrenheit_to_celsius(62))
print(converter.pounds_to_kg(3))
print(converter.kg_to_pounds(10))
print(converter.km_to_m(21))
print(converter.m_to_km(10))

# Импорт отдельных функций

from converter import fahrenheit_to_celsius, km_to_m, pounds_to_kg
print(fahrenheit_to_celsius(62))
print(km_to_m(21))
print(pounds_to_kg(3))

# Импорт с псевдонимом

import converter as cv
print(cv.celsius_to_fahrenheit(5))
print(cv.fahrenheit_to_celsius(62))
print(cv.pounds_to_kg(3))
print(cv.kg_to_pounds(10))
print(cv.km_to_m(21))
print(cv.m_to_km(10))