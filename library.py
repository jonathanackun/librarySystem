from books import Books
from members import Members

class Library:
    def __init__(self, memberCount, totalBookCount, currentBookCount, borrowedBooksCount):
        self.memberCount = memberCount
        self.totalBookCount = totalBookCount
        self.currentBookCount = currentBookCount
        self.borrowedBooksCount = borrowedBooksCount

    newBook = Books()
    newMember = Members()

    def newMember(self):
        self.memberCount += 1

    def newBook(self):
        self.totalBookCount += 1

    def lendBook(self):
        self.borrowedBooksCount += 1
        self.currentBookCount -= 1

    def returnBorrowedBook(self):
        self.borrowedBooksCount -= 1
        self.currentBookCount += 1