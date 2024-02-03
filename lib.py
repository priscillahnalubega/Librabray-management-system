class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
class Fiction(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn)
        self.genre = genre

    def display_info(self):
        return f"{super().display_info()}, Genre: {self.genre}"

class NonFiction(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

    def display_info(self):
        return f"{super().display_info()}, Subject: {self.subject}"
# Creating book instances
fiction_book = Fiction("1984", "George Orwell", "123456789", "Dystopian")
nonfiction_book = NonFiction("A Brief History of Time", "Stephen Hawking", "987654321", "Science")

# Displaying book information
print(fiction_book.display_info())
print(nonfiction_book.display_info())

