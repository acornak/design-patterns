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
import unittest
import typing

INDENT_SIZE = 2


class ClassBuilder:
    """
    Returns class
    """

    def __init__(self, class_name: str) -> None:
        """
        Constructor
        """
        self.class_name: str = class_name
        self.fields: list[FieldBuilder] = []

    def __str__(self) -> str:
        """
        String representation
        """
        lines: list[str] = [f"class {self.class_name}:"]
        indent: str = " " * INDENT_SIZE
        if not self.fields:
            lines.append(f"{indent}pass")
        else:
            lines.append(f"{indent}def __init__(self):")

            for field in self.fields:
                lines.append(f"{indent*2}{field}")

        return "\n".join(lines)


class FieldBuilder:
    """
    Builds class fields
    """

    def __init__(self, field_type: str, field_value: typing.Any) -> None:
        """
        Constructor
        """
        self.field_type: str = field_type
        self.field_value: typing.Any = field_value

    def __str__(self):
        """
        String representation
        """
        return f"self.{self.field_type} = {self.field_value}"


class CodeBuilder:
    """
    Codebuilder
    """

    def __init__(self, class_name: str) -> None:
        """
        Constructor
        """
        self.__class = ClassBuilder(class_name)

    def add_field(self, field_type: str, field_value: str) -> "CodeBuilder":
        """
        Add field
        """
        self.__class.fields.append(FieldBuilder(field_type, field_value))
        return self

    def __str__(self) -> str:
        """
        String representation
        """
        return self.__class.__str__()


class TestCodeBuild(unittest.TestCase):
    """
    Unit test
    """

    @staticmethod
    def preprocess(string: str = "") -> str:
        """
        Preprocess string
        """
        return string.strip().replace("\r\n", "\n")

    def test_empty(self):
        """
        Test empty class
        """
        generated_class = CodeBuilder("Foo")
        self.assertEqual(self.preprocess(str(generated_class)), "class Foo:\n  pass")

    def test_person(self):
        """
        Test class with methods
        """
        generated_class = (
            CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
        )
        self.assertEqual(
            self.preprocess(str(generated_class)),
            """class Foo:\n  def __init__(self):\n    self.name = \"\"\n    self.age = 0""",
        )


if __name__ == "__main__":
    unittest.main()
