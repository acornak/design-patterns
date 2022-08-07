"""
You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
The expected output of the above code is:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
Please observe the same placement of spaces and indentation.
"""


class CodeElement:
    """
    Create element of a code
    """

    indent_size = 2

    def __init__(
        self, class_name: str = None, field_type: str = None, field_value: str = None
    ) -> None:
        """
        Constructor
        """
        self.class_name = class_name
        self.field_type = field_type
        self.field_value = field_value
        self.elements: list = []

    def __compose_code(self) -> str:
        """
        Create properly indented element
        """
        lines: list[str] = []

        if self.class_name:
            lines.append(self.__create_class())
            lines.append(self.__create_init())
        else:
            lines.append(self.__create_variables())

        for elem in self.elements:
            # pylint: disable=W0212
            lines.append(elem.__compose_code())

        return "\n".join(lines)

    def __create_class(self) -> str:
        """
        Return class declaration and constructor
        """
        return f"class {self.class_name}:"

    def __create_init(self) -> str:
        """
        Assign variables
        """
        i = " " * self.indent_size
        return f"{i}def __init__(self):"

    def __create_variables(self) -> str:
        """
        Assign variables
        """
        i = " " * self.indent_size * 2
        return f"{i}self.{self.field_type} = {self.field_value}"

    def __str__(self) -> str:
        """
        String representation
        """
        return self.__compose_code()


class CodeBuilder:
    """
    Codebuilder
    """

    def __init__(self, class_name: str) -> None:
        """
        Constructor
        """
        self.class_name = class_name
        self.__class = CodeElement(class_name)

    def add_field(self, field_type: str, field_value: str) -> "CodeBuilder":
        """
        Add field
        """
        self.__class.elements.append(
            CodeElement(field_type=field_type, field_value=field_value)
        )
        return self

    def __str__(self) -> str:
        """
        String representation
        """
        return str(self.__class)


if __name__ == "__main__":
    cb = (
        CodeBuilder("Person").add_field("zidan", "sufurki").add_field("ja", "nevjeemus")
    )
    print(cb)
