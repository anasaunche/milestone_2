""" Format of the CSV file will be:
name,author,read/n
name,author,read/n
name,author,read/n
"""

books_file = 'books.txt'

def add_books(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0/n')

def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

        return [{'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]


def mark_books(name):
    pass






