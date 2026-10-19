class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # 1. __str__: Human-readable string representation (used by print() and str())
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # 2. __repr__: Unambiguous developer/debugging string representation
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    # 3. __len__: Enables the built-in len() function on instances
    def __len__(self):
        return self.pages

    # 4. __eq__: Overloads the equality operator (==)
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    # 5. __add__: Overloads the addition operator (+)
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented


b1 = Book("Fluent Python", "Luciano Ramalho", 800)
b2 = Book("Fluent Python", "Luciano Ramalho", 800)
b3 = Book("Clean Code", "Robert C. Martin", 464)

# Testing __str__ and __repr__
print(str(b1))          # 'Fluent Python' by Luciano Ramalho
print(repr(b1))         # Book(title='Fluent Python', author='Luciano Ramalho', pages=800)

# Testing __len__
print("Page count:", len(b1))  # 800

# Testing __eq__
print("b1 == b2:", b1 == b2)   # True
print("b1 == b3:", b1 == b3)   # False

# Testing __add__
print("Total pages:", b1 + b3)  # 1264