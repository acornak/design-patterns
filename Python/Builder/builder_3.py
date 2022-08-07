"""
Design pattern: Builder
"""


class Person:
    """
    Person class
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.name: str
        self.position: str
        self.date_of_birth: str

    def __str__(self) -> str:
        """
        String representation
        """
        return f"{self.name} born on {self.date_of_birth} and works as {self.position}."


class PersonBuilder:
    """
    Person builder
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.person = Person()

    def build(self) -> Person:
        """
        Builder
        """
        return self.person


class PersonInfoBuilder(PersonBuilder):
    """
    Person builder info
    """

    def called(self, name: str):
        """
        Add name
        """
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    """
    Person builder info
    """

    def works_as(self, position: str):
        """
        Add name
        """
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    """
    Person builder info
    """

    def born(self, date_of_birth: str):
        """
        Add name
        """
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == "__main__":
    pb = PersonBirthDateBuilder()
    me = pb.called("Anton").works_as("Engineer").born("1/1/1980").build()
    print(me)
