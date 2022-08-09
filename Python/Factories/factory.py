"""
Design pattern: Factory
"""
from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    """
    Coordinate system
    """

    CARTESIAN = 1
    POLAR = 2


class Point:
    """
    Point class
    """

    # def __init__(
    #     self, x: float, y: float, system: CoordinateSystem = CoordinateSystem.CARTESIAN
    # ) -> None:
    #     """
    #     Constructor
    #     """
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = x
    #         self.y = y
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = x * cos(y)
    #         self.y = x * sin(y)

    def __init__(self, x_point: float = 0, y_point: float = 0) -> None:
        """
        Constructor
        """
        self.x_point = x_point
        self.y_point = y_point

    def __str__(self) -> str:
        """
        String representation
        """
        return f"x: {self.x_point}, y: {self.y_point}"

    class PointFactory:
        """
        Point Factory subclass
        """

        def new_cartesian_point(self, x_point: float, y_point: float) -> "Point":
            """
            Create cartesian point
            """
            point = Point()
            point.x_point = x_point
            point.y_point = y_point
            return point

        def new_polar_point(self, rho: float, theta: float) -> "Point":
            """
            Create polar point
            """
            point = Point()
            point.x_point = rho * cos(theta)
            point.y_point = rho * sin(theta)
            return point

    factory = PointFactory()


if __name__ == "__main__":
    ppp = Point.factory.new_polar_point(2, 3)
    print(ppp)
