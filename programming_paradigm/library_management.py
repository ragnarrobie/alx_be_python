class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self.title} has not been checked out")
        else:
            print(f"{self.title} has been checked out.")
    def _return(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"{self.title} has been returned")
        else:
            self._is_checked_out = True
            print(f"{self.title} has not been checked out yet")

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    # Successfully checked out
                    return True
                else:
                    # Already checked out
                    return False
        # Book not found
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return True
                else:
                    # Book was not checked out
                    return False
        # Book not found
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")


    
        