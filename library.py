from catalogue import Catalogue


class Library:
    """
    This class represents a library.
    """
    def __init__(self):
        """
        Constructor for the Library class.
        Creates a Catalogue items.
        """
        self.library_catalogue = Catalogue()

    def get_catalogue(self):
        """
        Returns the Catalogue object.
        """
        return self.library_catalogue

    def display_available_items(self):
        """
        Displays all available items.
        """
        if not self.library_catalogue.item_list:
            print("No items available.")
        else:
            for item in self.library_catalogue.item_list:
                print("\n" + str(item))

    def check_out(self, call_number, null=None):
        """
        Checks out an item using the call number.
        If the item is not available, it prints a message.
        If the item is available, it decrements the number of available copies by 1.
        :param call_number: The call number of the item to be checked out.
        :param null: A null value to be used in place of the item.
        :return: None or the item to be checked out.
        """
        item = self.library_catalogue.find_item_by_callnum(call_number)
        if item == null:
            print(f"Item with call number {call_number} not found.")
            return
        if item.check_availability():
            item.num_of_copies -= 1
            print(f"Item with call number {call_number} checked out successfully.")
            return
        else:
            print(f"Item with call number {call_number} is not available for check out.")
            return

    def return_item(self, call_number):
        """
        Returns an item using the call number.
        If the item is not found, it prints a message.
        If the item is found, it increments the number of available copies by 1.
        :param call_number: The call number of the item to be returned.
        :return: None
        """
        for item in self.library_catalogue.item_list:
            if item.call_number == call_number:
                item.num_of_copies += 1
                print(f"Item with call number {call_number} returned successfully.")
                return
        print(f"Item with call number {call_number} not found.")

