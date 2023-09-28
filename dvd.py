from catalogueItem import CatalogueItem


class DVD(CatalogueItem):
    """
    This class inherits from CatalogueItem and represents a DVD that has a title, call number, number of copies,
    release date, and region code.
    """
    def __init__(self, title, call_number, num_of_copies, release_date, region_code):
        """
        Constructor for the DVD class.
        :param title: The title of the DVD.
        :param call_number: The call number of the DVD.
        :param num_of_copies: The number of copies of the DVD in the library.
        :param release_date: The release date of the DVD.
        :param region_code: The region code of the DVD.
        """
        super().__init__(title, call_number, num_of_copies)
        self.release_date = release_date
        self.region_code = region_code

    def get_type_specifics(self):
        """
        Returns the specifics of the DVD.
        :return: the release date and region code of the DVD.
        """
        return f"Release date: {self.release_date}\n" \
               f"Region code: {self.region_code}"
