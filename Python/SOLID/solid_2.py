"""
SOLID principles
2: Open-closed principle
"""
from enum import Enum


class Color(Enum):
    """
    Handles colors
    """

    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    """
    Handles sizes
    """

    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    """
    Handles productes
    """

    def __init__(self, name: str, color: Color, size: Size) -> None:
        """
        Constructor
        """
        self.name = name
        self.color = color
        self.size = size


# This is wrong:
# class ProductFilter:
#     """
#     Filters products
#     """

#     def filter_by_color(self, products: Product, color: Color) -> Product:
#         """
#         Filter based on color
#         """
#         for product in products:
#             if product.color == color:
#                 yield product

#     def filter_by_size(self, products: Product, size: Size) -> Product:
#         """
#         Filter based on size
#         """
#         for product in products:
#             if product.size == size:
#                 yield product


# OCP = open for extension, closed for modification
class Specification:
    """
    Check if items satisfies criteria
    """

    def is_satisfied(self, item: Product):
        """
        Empty method
        """

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    """
    Filtering
    """

    def filter(self, items: list[Product], spec: Specification):
        """
        Filter
        """


class ColorSpecification(Specification):
    """
    Check if color matches filter
    """

    def __init__(self, color: Color) -> None:
        """
        Constructor
        """
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    """
    Check if color matches filter
    """

    def __init__(self, size: Size) -> None:
        """
        Constructor
        """
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class ProductFilter(Filter):
    """
    Filter as it should be
    """

    def filter(self, items: list[Product], spec: Specification):
        """
        Override filter
        """
        for item in items:
            if spec.is_satisfied(item):
                yield item


class AndSpecification(Specification):
    """
    Combining filter with and
    """

    def __init__(self, *args) -> None:
        """
        Constructor
        """
        self.args = args

    def is_satisfied(self, item):
        """
        Override method
        """
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()

    print("Green products:")
    green = ColorSpecification(Color.GREEN)
    for p in pf.filter(products, green):
        print(f"{p.name} is green!")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in pf.filter(products, large):
        print(f"{p.name} is large!")

    print("Large blue items:")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in pf.filter(products, large_blue):
        print(f"{p.name} is large and blue!")

    print("Large green items:")
    large_green = large & ColorSpecification(Color.GREEN)
    for p in pf.filter(products, large_green):
        print(f"{p.name} is large and green!")
