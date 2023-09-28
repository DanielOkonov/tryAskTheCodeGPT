from catalogueItem import CatalogueItem


class Journal(CatalogueItem):
    """
    This class inherits from CatalogueItem and represents a Journal that has a title, call number, number of copies,
    author, issue number, and publisher.
    """
    def __init__(self, title, call_number, num_of_copies, author, issue_number, publisher, ):
        """
        Constructor for the Journal class.
        :param title: The title of the journal.
        :param call_number: The call number of the journal.
        :param num_of_copies: The number of copies of the journal in the library.
        :param author: The author of the journal.
        :param issue_number: The issue number of the journal.
        :param publisher: The publisher of the journal.
        """
        super().__init__(title, call_number, num_of_copies)
        self.author = author
        self.issue_number = issue_number
        self.publisher = publisher

    def get_type_specifics(self):
        """
        Returns the specifics of the journal.
        :return: The issue number and publisher of the journal.
        """
        return f"Issue number: {self.issue_number}\n" \
               f"Publisher: {self.publisher}"
