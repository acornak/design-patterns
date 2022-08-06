"""
SOLID principles
1: Single-responsibility principle
"""


class Journal:
    """
    Journal class
    """

    def __init__(self) -> None:
        """
        Initialize
        """
        self.entries = []
        self.count = 0

    def add_entry(self, text: str) -> None:
        """
        Add entry to the journal
        """
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos: int) -> None:
        """
        Remove entry from the journal
        """
        del self.entries[pos]
        self.count -= 1

    def __str__(self) -> str:
        """
        Override print method
        """
        return "\n".join(self.entries)

    # This is where it breaks the principle
    # def save(self, filename) -> None:
    #     """
    #     Save journal
    #     """
    #     file = open(filename, "w", encoding="")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename) -> None:
    #     """
    #     Load from file
    #     """

    # def load_from_web(self, uri) -> None:
    #     """
    #     Load from web address
    #     """


# Solution: create new class to handle new functionality
class PersistanceManager:
    """
    Manage the Journal
    """

    @staticmethod
    def save_to_file(journal: Journal, filename: str) -> None:
        """
        Save journal to file
        """
        file = open(filename, "w", encoding="utf8")
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    new_journal = Journal()
    new_journal.add_entry("This is the first entry.")
    new_journal.add_entry("Second day is also boring.")
    print(f"Journal entries: \n{new_journal}")

    PATH_TO_FILE = r"./journal.txt"
    PersistanceManager.save_to_file(new_journal, PATH_TO_FILE)
