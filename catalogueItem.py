from abc import ABC, abstractmethod


class CatalogueItem(ABC):
    """
    This is the abstract class for all items in the library.
    It contains the common properties of all items; title, call number, and number of copies.
    """

    @abstractmethod
    def __init__(self, title, call_number, num_of_copies):
        """
        Abstract class constructor.
        :param title: The title of the item.
        :param call_number: The call number of the item.
        :param num_of_copies: The number of copies of the item in the library.
        """
        self.title = title
        self.call_number = call_number
        self.num_of_copies = num_of_copies

    def check_availability(self):
        """
        Checks if the item is available.
        :return: True if the item is available, False otherwise.
        """""
        return self.num_of_copies > 0

    def __str__(self):
        """
        Returns a string representation of the item.
        :return: A string representation of the item.
        """
        return f"Type: {type(self)}\nTitle: {self.title}\nCall Number: {self.call_number}\nAvailable Copies: {self.num_of_copies}\n" \
               f"{self.get_type_specifics()}"
