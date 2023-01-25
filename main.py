from utils import database

USER_CHOICE = """
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark book as read
-'d' to delete a book
-'q' to quit

"""


def prompt_add_book():
    name = input('Please add a book: ')
    author = input('please add the author of this book')

    database.add_books(name, author)

def list_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} - read: {read}")


def prompt_mark_as_read():
    pass


def prompt_delete():
    pass


def menu():
    user_selection = input(USER_CHOICE)
    while user_selection != 'q':
        if user_selection == 'a':
            prompt_add_book()
        elif user_selection == 'l':
            list_books()
        elif user_selection == 'r':
            prompt_mark_as_read()
        elif user_selection == 'd':
            prompt_delete()
        else:
            break

        user_selection = input(USER_CHOICE)

menu()










