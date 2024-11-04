# Library Management System

This Library Management System is a simple Python program that allows users to manage books and members in a library. It enables members to check out and return books, keeping track of the availability of each book and the books each member has checked out.

## Features

- **Book Management**: Add books with title, author, ISBN, and availability status.
- **Member Management**: Register members with names and unique IDs.
- **Checkout and Return**: Members can check out available books and return them.
- **Display Books**: List all books in the library along with their availability status.

## Classes

### Book

- Represents a book in the library.
- Attributes:
  - `title`: The title of the book.
  - `author`: The author of the book.
  - `isbn`: The ISBN number of the book.
  - `available`: The availability status of the book (default is `True`).

- Methods:
  - `checkout()`: Marks the book as unavailable.
  - `return_book()`: Marks the book as available.
  - `__repr__()`: Returns a string representation of the book.
  - `__str__()`: Returns a more readable string representation of the book.

### Member

- Represents a member of the library.
- Attributes:
  - `name`: The name of the member.
  - `member_id`: A unique identifier for the member.
  - `checked_out_books`: A list of books checked out by the member.

- Methods:
  - `checkout_book(book)`: Checks out a book for the member.
  - `return_book(book)`: Returns a book checked out by the member.
  - `__str__()`: Returns a string representation of the member and their checked-out books.

### Library

- Represents the library itself.
- Attributes:
  - `books`: A list of books in the library.
  - `members`: A list of members of the library.

- Methods:
  - `add_book(book)`: Adds a book to the library.
  - `add_member(member)`: Adds a member to the library.
  - `checkout_book(member_id, isbn)`: Allows a member to check out a book by ISBN.
  - `return_book(member_id, isbn)`: Allows a member to return a checked-out book by ISBN.
  - `display_books()`: Displays all books in the library along with their availability status.

## Installation

To run the Library Management System, you need to have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).


