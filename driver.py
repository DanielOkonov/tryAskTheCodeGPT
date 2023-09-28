from library import Library

"""
This is the driver file for the library.
"""


def main():
    """
    This is the main driver function for the library.
    """
    my_library = Library()

    catalogue = my_library.get_catalogue()

    catalogue.add_item()

    catalogue.add_item()

    my_library.display_available_items()

    user_input = input("What's the call number of the item you want to check out?")
    user_input_int = int(user_input)

    my_library.check_out(user_input_int)

    my_library.check_out(user_input_int)

    my_library.display_available_items()

    my_library.return_item(user_input_int)

    my_library.display_available_items()

    print("Test find by call num and title")

    returned_item = catalogue.find_item_by_callnum(user_input_int)

    print(str(returned_item))


if __name__ == "__main__":
    main()
