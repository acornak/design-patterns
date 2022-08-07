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
        # Address
        self.street_address: str
        self.postcode: str
        self.city: str
        # Employment
        self.company_name: str
        self.position: str
        self.annual_income: str

    def __str__(self) -> str:
        """
        String representation
        """
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}"
            + f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"
        )


class PersonBuilder:
    """
    Person builder
    """

    def __init__(self, person: Person = Person()) -> None:
        """
        Constructor
        """
        self.person = person

    def build(self) -> Person:
        """
        Build method
        """
        return self.person


class PersonJobBuilder(PersonBuilder):
    """
    Person job builder
    """

    def __init__(self, person: Person) -> None:
        """
        Constructor
        """
        super().__init__(person)

    def works_at(self, company_name: str) -> "PersonJobBuilder":
        """
        Add company
        """
        self.person.company_name = company_name
        return self

    def works_as(self, position: str) -> "PersonJobBuilder":
        """
        Add position
        """
        self.person.position = position
        return self
