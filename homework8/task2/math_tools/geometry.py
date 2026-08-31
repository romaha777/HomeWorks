#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Функция для расчёта площади прямоугольника

def rectangle_area(a,b):
    """
    Функция находит площадь прямоугольника

    Формула: S = a * b
                
    Пример:
        >>> rectangle_area(3,2)
        6
        >>> rectangle_area(11,4)
        44
    """
    return a * b

# Функция для расчёта площади прямоугольника

def circle_area(r):
    """
    Функция находит площадь прямоугольника
    
    Формула: S = pi * r ** 2
                    
    Пример:
        >>> circle_area(4)
        50.2654824
        >>> circle_area(12)
        452.3893416
    """
    pi = 3.14159265
    return pi * r ** 2

# Функция для расчёта периметра прямоугольника

def rectangle_perimetr(a,b):
    """
    Функция находит периметр прямоугольника
        
    Формула: P = 2 * (a + b)
                        
    Пример:
        >>> rectangle_perimetr(2,4)
        12
        >>> rectangle_perimetr(20,5)
        50
    """
    return 2 * (a + b)