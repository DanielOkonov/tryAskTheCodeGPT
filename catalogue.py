from catalogueItem import CatalogueItem
from libraryItemGenerator import LibraryItemGenerator


class Catalogue(CatalogueItem):
    """
    This class inherits from CatalogueItem and represents a catalogue of items with a list of items.
    """
    def __init__(self):
        """
        Constructor for the Catalogue class.
        Creates an empty list of items.
        Creates a LibraryItemGenerator object.
        """
        self.item_list = []
        self.item_generator = LibraryItemGenerator()

    def find_item(self, string):
        """
        This method searches through the list of items and returns the item
        with the matching title.
        :param string: The title of the item to be found.
        :return: The item with the matching title.
        """
        for item in self.item_list:
            if string.lower() in item.title.lower():
                return item
        return

    def find_item_by_callnum(self, call_number):
        """
        This method searches through the list of items and returns the item
        with the matching call number.
        :param call_number: The call number of the item to be found.
        :return: The item with the matching call number.
        """
        for item in self.item_list:
            if call_number == item.call_number:
                return item
        return

    def add_item(self):
        """
        This method adds a new item to the list of items.
        """
        self.item_list.append(self.item_generator.create_library_item())

    def remove_item(self, call_number):
        """
        This method removes an item from the list of items.
        :param call_number: The call number of the item to be removed.
        """
        for item in self.item_list:
            if item.call_number == call_number:
                self.item_list.remove(item)
                print(f"Item with call number {call_number} removed.")
                return
        print(f"Item with call number {call_number} not found.")
