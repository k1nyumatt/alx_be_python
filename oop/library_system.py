class Book:
    """
    Base class representing a book.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    
    Attributes:
        title (str): The title of the book (inherited)
        author (str): The author of the book (inherited)
        file_size (int): The file size in KB
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    
    Attributes:
        title (str): The title of the book (inherited)
        author (str): The author of the book (inherited)
        page_count (int): The number of pages in the book
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class representing a library that holds a collection of books.
    
    Attributes:
        books (list): A list storing Book, EBook, and PrintBook instances
    """
    
    def __init__(self):
        """Initialize a Library with an empty books list."""
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)


# Example usage
if __name__ == "__main__":
    # Create a library
    my_library = Library()
    
    # Create different types of books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook1 = EBook("1984", "George Orwell", 2048)
    printbook1 = PrintBook("To Kill a Mockingbird", "Harper Lee", 324)
    ebook2 = EBook("The Hobbit", "J.R.R. Tolkien", 3072)
    printbook2 = PrintBook("Pride and Prejudice", "Jane Austen", 432)
    
    # Add books to the library
    print("Adding books to the library:")
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(printbook1)
    my_library.add_book(ebook2)
    my_library.add_book(printbook2)
    
    # List all books
    my_library.list_books()