"""
You are given a class called Person . The person has two attributes: id , and name .

Please implement a  PersonFactory that has a non-static  create_person()
method that takes a person's name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created.
So, the first person the factory makes should have Id=0, second Id=1 and so on.
"""
import unittest


class Person:
    """
    Person class
    """

    def __init__(self, id_number: int, name: str) -> None:
        """
        Constructor
        """
        self.id_number: int = id_number
        self.name: str = name


class PersonFactory:
    """
    Factory method for person class
    """

    id_number = 0

    def create_person(self, name: str) -> Person:
        """
        Create p erson method
        """
        res = Person(self.id_number, name)
        self.id_number += 1
        return res


class PersonTestCase(unittest.TestCase):
    """
    Unit test for person class
    """

    def test_person(self):
        """
        Basic test
        """
        factory = PersonFactory()

        person1 = factory.create_person("Chris")
        self.assertEqual(person1.name, "Chris")
        self.assertEqual(person1.id_number, 0)

        person2 = factory.create_person("Sarah")
        self.assertEqual(person2.name, "Sarah")
        self.assertEqual(person2.id_number, 1)


if __name__ == "__main__":
    unittest.main()
