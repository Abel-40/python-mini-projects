class Book:
  def __init__(self, title,author,isbn,available = True):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available = available

  def checkout(self):
    self.available = False

  def return_book(self):
    self.available = True

  def __repr__(self):
    return f"Book(Book Title: {self.title} \n Author: {self.author} \n Isbn: {self.isbn} \n available: {self.available})"

  def __str__(self):
    return f"Book Title: {self.title} \n Author: {self.author} \n Isbn: {self.isbn} \n available: {self.available}"


class Member:
    def __init__(self, name, member_id, checked_out_books=None):
        if checked_out_books is None:
            checked_out_books = [] 
        self.name = name
        self.member_id = member_id
        self.checked_out_books = checked_out_books

    def checkout_book(self,book):
      if book.available:
        self.checked_out_books.append(book)
        book.checkout()
        print(f"{self.name} has checked out '{book.title}'.")
      else:
        print(f"Sorry, '{book.title}' is not available for checkout.")
    
    def return_book(self,book):
      if book.available == False:
        self.checked_out_books.remove(book)
        book.return_book()
        print(f"{self.name} has return the book '{book.title}'.")
      else:
        print(f"The book is still available try to checkout the book")
    def __str__(self):
      list_of_book = ''
      for books in self.checked_out_books:
        list_of_book += books
      return f"{self.name} checked out {list_of_book}"


class Library:
  def __init__(self, books=None, members=None):
    if books is None:
      books = []
    if members is None:
      members = []
    self.books = books
    self.members = members

  def add_book(self, book):
    self.books.append(book)

  def add_member(self, member):
    self.members.append(member)

  def checkout_book(self, member_id, isbn):
    # Find the member by member_id
    
    member = next((m for m in self.members if m.member_id == member_id), None)
    if member is None:
      print("Member not found.")
      return
    
    # Find the book by isbn
    book = next((b for b in self.books if b.isbn == isbn), None)
    if book is None:
      print("Book not found.")
      return

    # Checkout the book using Member's method
    member.checkout_book(book)

  def return_book(self, member_id, isbn):
    # Find the member by member_id
    member = next((m for m in self.members if m.member_id == member_id), None)
    if member is None:
      print("Member not found.")
      return
    
    # Find the book by isbn
    book = next((b for b in self.books if b.isbn == isbn), None)
    if book is None:
      print("Book not found.")
      return

    # Return the book using Member's method
    member.return_book(book)

  def display_books(self):
    for n, book in enumerate(self.books):
      print(f"{n+1}, Book Title: {book.title} author: {book.author} availabilty: {book.available}")


book1 = Book("harry potter","Abel addis","978-0-98-098")
book2 = Book("The Hobbit", "J.R.R. Tolkien", "978-0-00-0002")
book3 = Book("1984", "George Orwell", "978-0-45-0456")
book4 = Book("Pride and Prejudice", "Jane Austen", "978-0-33-3334")
book5 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-5432", False)
book6 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-74-3274")
book7 = Book("Moby Dick", "Herman Melville", "978-0-14-2437", False)


member1 = Member("Abel","nsr/020/14")
member2 = Member("Betty", "nsr/021/15")
member3 = Member("John", "nsr/022/16")
member4 = Member("Alice", "nsr/023/17")
member5 = Member("Michael", "nsr/024/18")
member6 = Member("Sarah", "nsr/025/19")
member7 = Member("David", "nsr/026/20")

books = [book1, book2, book3, book4, book5, book6, book7]
members = [member1, member2, member3, member4, member5, member6, member7]
library = Library(books,members)

# Display all books in the library
print("Initial Library Books:")
library.display_books()
print("\n")

# Member 1 (Abel) checks out "Harry Potter"
library.checkout_book("nsr/020/14", "978-0-98-098")

# Member 2 (Betty) tries to check out "To Kill a Mockingbird", which is already unavailable
library.checkout_book("nsr/021/15", "978-0-06-5432")

# Member 2 (Betty) checks out "The Hobbit"
library.checkout_book("nsr/021/15", "978-0-00-0002")

# Display all books after checkout
print("\nLibrary Books After Checkout:")
library.display_books()
print("\n")

# Member 1 (Abel) returns "Harry Potter"
library.return_book("nsr/020/14", "978-0-98-098")

# Display all books after return
print("\nLibrary Books After Return:")
library.display_books()
print("\n")

# Check which books each member has checked out
print(f"Abel's checked out books: {[book.title for book in member1.checked_out_books]}")
print(f"Betty's checked out books: {[book.title for book in member2.checked_out_books]}")


