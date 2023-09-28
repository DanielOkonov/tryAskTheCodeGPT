from catalogueItem import CatalogueItem


class Book(CatalogueItem):
    """
    This class inherits from CatalogueItem and represents a book that has a title, call number, and author.
    """
    def __init__(self, title, call_number, num_of_copies, author):
        super().__init__(title, call_number, num_of_copies)
        self.author = author

        """
        Book class constructor.
        :param title: The title of the book.
        :param call_number: The call number of the book.
        :param num_of_copies: The number of copies of the book in the library.
        :param author: The author of the book.
        """

    def get_type_specifics(self):
        """
        Returns the specifics of the book.
        :return: The author of the book.
        """
        return f"Author: {self.author}"
