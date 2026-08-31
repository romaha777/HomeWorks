#!/usr/bin/python3

# -*- coding: utf-8 -*-

import math_tools

print(math_tools.add(4,5))
print(math_tools.rectangle_area(6,5))
print(math_tools.mean([2, 3, 5, 8, 1]))


from math_tools import subtract, multiply, circle_area, median

print(subtract(10,7))
print(multiply(4,10))
print(circle_area(20))
print(median([15, 8, 2, 6, 8]))


import math_tools as mt

print(mt.divide(15,5))
print(mt.rectangle_perimetr(2,10))