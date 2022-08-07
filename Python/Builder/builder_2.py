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
        self.annual_income: int

    def __str__(self) -> str:
        """
        String representation
        """
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}.\n"
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

    @property
    def works(self) -> "PersonJobBuilder":
        """
        Works
        """
        return PersonJobBuilder(self.person)

    @property
    def lives(self) -> "PersonAddressBuilder":
        """
        Works
        """
        return PersonAddressBuilder(self.person)

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

    def at(self, company_name: str) -> "PersonJobBuilder":
        """
        Add company
        """
        self.person.company_name = company_name
        return self

    def as_a(self, position: str) -> "PersonJobBuilder":
        """
        Add position
        """
        self.person.position = position
        return self

    def earning(self, annual_income: int) -> "PersonJobBuilder":
        """
        Add annual income
        """
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    """
    Person addres builder
    """

    def __init__(self, person: Person) -> None:
        """
        Constructor
        """
        super().__init__(person)

    def at(self, street_address: str) -> "PersonAddressBuilder":
        """
        Add street address
        """
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode: str) -> "PersonAddressBuilder":
        """
        Add postcode
        """
        self.person.postcode = postcode
        return self

    def in_city(self, city: str) -> "PersonAddressBuilder":
        """
        Add city
        """
        self.person.city = city
        return self


if __name__ == "__main__":
    pb = PersonBuilder()
    test_person = (
        pb.lives.at("123 London Road")
        .in_city("London")
        .with_postcode("SW12BC")
        .works.at("Fabrikam")
        .as_a("Engineer")
        .earning(123000)
        .build()
    )
    print(test_person)
