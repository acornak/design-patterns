"""
SOLID principles
4: Interface segregation principle
"""


from abc import abstractmethod


class Machine:
    """
    Interface
    """

    def print(self, document: str) -> None:
        """
        Print func
        """
        raise NotImplementedError

    def fax(self, document: str) -> None:
        """
        Fax func
        """
        raise NotImplementedError

    def scan(self, document: str) -> None:
        """
        Scan func
        """
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    """
    Implementation of multifunction printer
    """

    def print(self, document: str) -> None:
        """
        Print func
        """

    def fax(self, document: str) -> None:
        """
        Fax func
        """

    def scan(self, document: str) -> None:
        """
        Scan func
        """


class OldFashionedPrinter(Machine):
    """
    Old machine
    """

    def print(self, document: str) -> None:
        """
        Print func
        """
        # OK

    def fax(self, document: str) -> None:
        """
        Fax func
        """
        # noop

    def scan(self, document: str) -> None:
        """
        Scan func - NOT SUPPORTED
        """
        raise NotImplementedError("Printer cannot scan!")


# Better way
class Printer:
    """
    Printer class
    """

    @abstractmethod
    def print(self, document: str) -> None:
        """
        Print method
        """


class Scanner:
    """
    Scanner class
    """

    @abstractmethod
    def scan(self, document: str) -> None:
        """
        Scan method
        """


class MyPrinter(Printer):
    """
    Printer only
    """

    def print(self, document: str) -> None:
        """
        Print method
        """


class MyScanner(Scanner):
    """
    Printer only
    """

    def scan(self, document: str) -> None:
        """
        Print method
        """


class Photocopier(Printer, Scanner):
    """
    Both printing and scanning
    """

    def print(self, document: str) -> None:
        """
        Print method
        """
        print(document)

    def scan(self, document: str) -> None:
        """
        Scan method
        """


# Even better
class MultiFunctionDevice(Printer, Scanner):
    """
    Interface for Multifunctional device
    """

    @abstractmethod
    def print(self, document: str) -> None:
        """
        Print method
        """

    @abstractmethod
    def scan(self, document: str) -> None:
        """
        Scan method
        """


class MultiFunctionMachine(MultiFunctionDevice):
    """
    Implementation of interface for Multifunctional device
    """

    def __init__(self, printer, scanner) -> None:
        """
        Constructor
        """
        self.printer = printer
        self.scanner = scanner

    def print(self, document: str) -> None:
        """
        Print implementation
        """
        self.printer.print(document)

    def scan(self, document: str) -> None:
        """
        Print implementation
        """
        self.scanner.scan(document)


if __name__ == "__main__":
    device = MultiFunctionMachine(MyPrinter(), MyScanner())
    device.print("123")
