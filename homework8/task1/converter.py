#!/usr/bin/python3

# -*- coding: utf-8 -*-

def celsius_to_fahrenheit(celsius):
    """
    Переводит градусы Цельсия в градусы Фаренгейта.
    
    Формула: F = (9 * C / 5) + 32
    
    Пример:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return round((9 * celsius / 5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    """
    Переводит градусы Фаренгейта в градусы Цельсия.
    
    Формула: C = (F - 32) * 5 / 9

    Пример:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    return round((fahrenheit - 32) * 5 / 9, 2)

def km_to_m(km):
    """
    Переводит километры в мили.

    1 км примерно равен 0,621371 мили

    Пример:
        >>> kilometers_to_miles(1)
        0.62
        >>> kilometers_to_miles(10)
        6.21
    """
    return round(km * 0.621371, 2)

def m_to_km(m):
    """
    Переводит мили в километры.

    1 миля примерно равна 1,60934 км

    Пример:
        >>> miles_to_kilometers(1)
        1.61
        >>> miles_to_kilometers(5)
        8.05
    """
    return round(m * 1.60934, 2)

def kg_to_pounds(kg):
    """
    Переводит килограммы в фунты.

    1 кг примерно равен 2,20462 фунта

    Пример:
        >>> kilograms_to_pounds(1)
        2.2
        >>> kilograms_to_pounds(5)
        11.02
    """
    return round(kg * 2.20462, 2)

def pounds_to_kg(pounds):
    """
    Переводит фунты в килограммы.

    1 фунт примерно равен 0,453592 кг

    Пример:
        >>> pounds_to_kilograms(1)
        0.45
        >>> pounds_to_kilograms(2.2)
        1.0
    """
    return round(pounds * 0.453592, 2)