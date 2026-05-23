#!/usr/bin/python3

# -*- coding: utf-8 -*-

sales_data = [
    ("яблоки", "фрукты", 50.0, 10),
    ("бананы", "фрукты", 70.0, 5),
    ("молоко", "молочные", 80.0, 8),
    ("сыр", "молочные", 200.0, 3),
    ("хлеб", "выпечка", 40.0, 12)
]

category_dict = {}
category_dict2 = {}

# Создаю словарь, где ключ - категория продуктов,
# а значения - списки кортежей (название товара, выручка от товара)

for product, category, cost, amount in sales_data:
    revenue = cost * amount
    if category not in category_dict:
        category_dict[category] = []
    category_dict[category].append((product, revenue))

# Создаю новый словарь, где ключ - категория продуктов,
# а значение - словарь, в котором ключ - информация по общей выручке
# и среднему чеку, а значение - стоимость

for category, product_list in category_dict.items():
    total_revenue = 0
    count = 0
    for product, revenue in product_list:
        total_revenue += revenue
        count += 1
    avg_check = total_revenue / count
    category_dict2[category] = {
        "total_revenue": total_revenue, "avg_check": avg_check,
    }

    # Вычисляю категорию с максимальной общей выручкой

    best_category = max(category_dict2.items(), key=lambda x: x[1]["total_revenue"])


print(category_dict2)
print(f"Категория с максимальной общей выручкой: {best_category[0]}")