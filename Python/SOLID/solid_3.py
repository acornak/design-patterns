# type: ignore
"""
SOLID principles
3: Liskov Substitution principle
"""


class Rectangle:
    """
    Rectangle
    """

    def __init__(self, height: int, width: int) -> None:
        """
        Constructor
        """
        self._height = height
        self._width = width

    @property
    def width(self) -> int:
        """
        Width
        """
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """
        Width setter
        """
        self._width = value

    @property
    def height(self) -> int:
        """
        Width
        """
        return self._height

    @height.setter
    def height(self, value) -> None:
        """
        Width setter
        """
        self._height = value

    @property
    def area(self) -> int:
        """
        Calculate area
        """
        return self._width * self._height

    def __str__(self):
        """
        String representation
        """
        return f"Width: {self.width}, Height: {self.height}, Area: {self.area}"


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size: int) -> None:
        """
        Constructor
        """
        Rectangle.__init__(self, size, size)

    # This is direct violation of Liskov substitution principle
    @Rectangle.width.setter
    def width(self, value: int) -> None:
        """
        Square width
        """
        self._width = self._height = value

    # This is direct violation of Liskov substitution principle
    @Rectangle.height.setter
    def height(self, value: int) -> None:
        """
        Square width
        """
        self._height = self._width = value


def use_it(rect):
    """
    Use rectangle
    """
    width = rect.width
    rect.height = 10
    expected = int(width * 10)
    print(f"expected an area of {expected}, got {rect.area}")


if __name__ == "__main__":
    new_rect = Rectangle(2, 3)
    use_it(new_rect)

    sq = Square(5)
    use_it(sq)
