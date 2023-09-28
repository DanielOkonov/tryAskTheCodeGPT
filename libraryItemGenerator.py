from book import Book
from journal import Journal
from dvd import DVD


class LibraryItemGenerator:
    """
    This class is used to create a new library item.
    """
    def __init__(self):
        """
        Constructor for the LibraryItemGenerator class.
        """
        pass

    def create_library_item(self):
        """
        This method is used to prompt the user to create a new library item.
        :return: A new library item.
        """
        pass
        print("Hello librarian! Please follow these prompts to create a new item.")
        user_item_select = input("Select an item type to create:\n"
                                 "1 - Book\n"
                                 "2 - Journal\n"
                                 "3 - DVD\n")

        if user_item_select == "1":
            user_title_select = input("You have selected the book option, what is the title "
                                      "of the book you want to add?\n")

            user_call_number = input("What would you like the call number of this book to be?\n")
            int_call_number = int(user_call_number)

            user_num_of_copies = input("How many copies of this book are there in this library?\n")
            int_num_of_copies = int(user_num_of_copies)

            user_author_name = input("What's the name of the author who wrote this book?\n")

            return Book(user_title_select, int_call_number, int_num_of_copies, user_author_name)

        if user_item_select == "2":
            user_title_select = input("You have selected the Journal option, what is the title "
                                      "of the Journal you want to add?\n")

            user_call_number = input("What would you like the call number of this Journal to be?\n")
            int_call_number = int(user_call_number)

            user_num_of_copies = input("How many copies of this Journal are there in this library?\n")
            int_num_of_copies = int(user_num_of_copies)

            user_author_name = input("What's the name of the author who wrote this Journal?\n")

            user_issue_number = input("What's the issue number of this Journal?\n")
            int_issue_number = int(user_issue_number)

            user_publisher = input("What's the name of the publisher of this Journal?\n")

            return Journal(user_title_select, int_call_number, int_num_of_copies, user_author_name, int_issue_number,
                           user_publisher)

        if user_item_select == "3":
            user_title_select = input("You have selected the DVD option, what is the title of the "
                                      "DVD you want to add?\n")

            user_call_number = input("What would you like the call number of this DVD to be?\n")
            int_call_number = int(user_call_number)

            user_num_of_copies = input("How many copies of this DVD are there in this library?\n")
            int_num_of_copies = int(user_num_of_copies)

            user_release_date = input("What is the release date of this DVD?\n")

            user_region_code = input("What is the region code of this DVD?\n")

            return DVD(user_title_select, int_call_number, int_num_of_copies, user_release_date, user_region_code)
