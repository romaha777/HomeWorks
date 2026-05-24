#!/usr/bin/python3

# -*- coding: utf-8 -*-

def calculate_calories(product, calories_per_100g, weight):
    result = (calories_per_100g * weight) / 100
    return print(f"В {weight} г {product} содержится {result} калорий.")

calculate_calories("пивчик", 45, 500)

# Думаю, пивчик тоже не требует объяснений