#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Функция расчета среднего арифметического

def mean(values):
    """
    Функция находит среднее арифметическое чисел из списка
            
    Пример:
        >>> print(mean([1, 2, 3, 4, 5]))
        3.0
    """
    if not values:
        raise ValueError("Пустой список")
    return sum(values) / len(values)

# Функция расчета медиана

def median(values):
    """
    Функция находит медиан из списка
                
    Пример:
        >>> print(median([7, 1, 3, 9, 5]))
        5
        >>> print(median([1, 2, 3, 4]))
        2.5
    """
    if not values:
        raise ValueError("Пустой список")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    # Если нечётное количество элементов — берём центральный
    if n % 2 == 1:
        return sorted_vals[mid]
    # Если чётное — среднее двух центральных
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2