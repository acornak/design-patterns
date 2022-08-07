"""
Design pattern: Builder
"""


class HtmlElement:
    """
    Class to create HTML content
    """

    indent_size = 2

    def __init__(self, name: str = "", text: str = "") -> None:
        """
        Constructor
        """
        self.text = text
        self.name = name
        self.elements: list = []

    def __str(self, indent: int) -> str:
        """
        Private member for indentation
        """
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i_1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i_1}{self.text}")

        for elem in self.elements:
            # pylint: disable=W0212
            lines.append(elem.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        """
        String representation
        """
        print(self.elements)
        return self.__str(0)

    @staticmethod
    def create(name: str):
        """
        Build
        """
        return HtmlBuilder(name)


class HtmlBuilder:
    """
    HTML Builder class
    """

    def __init__(self, root_name: str) -> None:
        """
        Constructor
        """
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)
        print(self.__root)

    def add_child(self, child_name: str, child_text: str):
        """
        Append new html element
        """
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name: str, child_text: str) -> "HtmlBuilder":
        """
        Append new html element
        """
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self) -> str:
        """
        String representation
        """
        return str(self.__root)


if __name__ == "__main__":
    builder = HtmlBuilder("ui")
    builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
    print("Fluent builder:")
    print(builder)
