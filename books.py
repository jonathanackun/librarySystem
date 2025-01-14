class Books:
    def __init__(self, title, authour, availability):
        self.title = title
        self.authour = authour
        self.availability = availability

    def __str__(self):
        return f"Book Title: {self.title}, Book Author: {self.authour}"