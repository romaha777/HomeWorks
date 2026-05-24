#!/usr/bin/python3

# -*- coding: utf-8 -*-

def weather_report(temperature, condition = "ясно"):
    char = "морозно" if temperature < 0 else "прохладно" if temperature <= 15 else "комфортно" if temperature <= 25 else "жарко"
    return f"Сегодня {char}, {condition}, температура {temperature}°C"

print(weather_report(28))

print(weather_report(-5, "снег"))

print(weather_report(18, "облачно"))

print(weather_report(8))

# Это лучшая домашка за всё время)