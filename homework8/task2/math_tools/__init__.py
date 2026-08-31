#!/usr/bin/python3

# -*- coding: utf-8 -*-

__version__ = "1.0.0"

from .basic import add, subtract, multiply, divide
from .geometry import rectangle_area, rectangle_perimetr, circle_area
from .statistics import mean, median

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "rectangle_area",
    "rectangle_perimetr",
    "circle_area",
    "mean",
    "median",
    "variance",
    "__version__",
]