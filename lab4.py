from functools import partial


PRODUCTS = (
    {"name": "Laptop", "category": "electronics", "price": 1200},
    {"name": "Mouse", "category": "electronics", "price": 40},
    {"name": "Desk", "category": "furniture", "price": 300},
    {"name": "Chair", "category": "furniture", "price": 150},
)

NUMBERS = (1, 5, 10, 15, 20)


# Уровень 1
filter_by = (
    lambda key:
    lambda value:
    lambda items: [
        item
        for item in items
        if item[key] == value
    ]
)


# Уровень 2
def filter_by_key(key: str, value: object, items: list[dict] | tuple[dict, ...]) -> list[dict]:
    return filter_by(key)(value)(items)


filter_by_category = partial(filter_by_key, "category")


# Уровень 3
greater_than = (
    lambda threshold:
    lambda x: x > threshold
)

numbers_greater_than_10 = list(filter(greater_than(10), NUMBERS))


# Примеры использования
ELECTRONICS = filter_by("category")("electronics")(PRODUCTS)
FURNITURE = filter_by_category("furniture", PRODUCTS)


# Уровень 4
# Каррирование позволило собирать специализированные функции из более общей:
# например, сначала зафиксировать ключ "category", а потом переиспользовать
# получившийся фильтр с разными значениями и списками.
#
# Без каррирования можно было обойтись, передавая все аргументы сразу. Но тогда
# было бы менее удобно создавать маленькие переиспользуемые функции для filter,
# partial и композиции.
