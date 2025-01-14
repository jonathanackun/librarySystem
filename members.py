class Members:
    def __init__(self, name, memberId, borrowedBooks):
        self.name = name
        self.memberId = memberId
        self.borrowedBooks = borrowedBooks

    def __str__(self):
        return f"Member Name: {self.name}, Member ID: {self.memberId}"