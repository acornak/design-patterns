"""
SOLID principles
5: Dependency inversion principle
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    """
    Defines relationship
    """

    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    """
    Person class
    """

    def __init__(self, name: str) -> None:
        """
        Initialization
        """
        self.name = name


class RelationshipBrowser:
    """
    Remove dependency on data type in Relationship class
    """

    @abstractmethod
    def find_all_children_of(self, name: str) -> None:
        """
        Find all children based on parent name
        """


class Relationships(RelationshipBrowser):
    """
    Relationships
    """

    def __init__(self) -> None:
        """
        Initialization
        """
        # this is issue
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person) -> None:
        """
        Add parent:child relationship
        """
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name: str) -> None:
        """
        Implementation
        """
        for relation in self.relations:
            if relation[0].name == name and relation[1] == Relationship.PARENT:
                yield relation[2].name


class Research:
    """
    Research
    """

    # def __init__(self, relationships: Relationship) -> None:
    #     """
    #     Initialization
    #     """
    #     relations = relationships.relations
    #     for relation in relations:
    #         if relation[0].name == "John" and relation[1] == Relationship.PARENT:
    #             print(f"John has a child called {relation[2].name}")

    def __init__(self, browser: RelationshipBrowser) -> None:
        for child in browser.find_all_children_of("John"):
            print(f"John has a child called {child}")


if __name__ == "__main__":
    father = Person("John")
    child1 = Person("Chris")
    child2 = Person("M?att")

    rel = Relationships()
    rel.add_parent_and_child(father, child1)
    rel.add_parent_and_child(father, child2)

    Research(rel)
