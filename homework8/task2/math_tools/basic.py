#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Функция суммы

def add(a,b):
    """
    Складывает a и b
    
    Пример:
        >>> add(1,2)
        3
        >>> add(11,25)
        36
    """
    return a + b

# Функция разности

def subtract(a,b):
    """
    Вычитает b из a
        
    Пример:
        >>> subtract(3,2)
        1
        >>> subtract(43,25)
        18
    """
    return a - b

# Функция произведения

def multiply(a,b):
    """
    Умножает a на b
            
    Пример:
        >>> multiply(3,2)
        6
        >>> multiply(11,4)
        44
    """
    return a * b

# Функция деления

def divide(a,b):
    """
    Делит a на b
                
    Пример:
        >>> divide(4,2)
        2
        >>> divide(28,7)
        4
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b