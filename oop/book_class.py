class Book:
    """
    A class to represent a book with title, author, and publication year.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        year (int): The publication year of the book
    """
    
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method called when the object is deleted.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Return a user-friendly string representation of the book.
        
        Returns:
            str: Formatted string with book details
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Return an official string representation that can recreate the object.
        
        Returns:
            str: String that represents the Book constructor call
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (you can uncomment to test)
if __name__ == "__main__":
    # Create a book instance
    book1 = Book("1984", "George Orwell", 1949)
    
    # Test __str__ method
    print("Using print (calls __str__):")
    print(book1)
    
    # Test __repr__ method
    print("\nUsing repr (calls __repr__):")
    print(repr(book1))
    
    # Create another book
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    print(f"\nCreated: {book2}")
    
    # Delete a book (calls __del__)
    print("\nDeleting book2...")
    del book2
    
    print("\nScript ending (book1 will be deleted automatically)...")