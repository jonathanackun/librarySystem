from books import Books
from members import Members

class Library:
    def __init__(self):
        self.memberCount = 0
        self.totalBookCount = 0
        self.currentBookCount = 0
        self.borrowedBooksCount = 0
        self.borrowedBookName = []
        self.books = []
        self.members = []

    def newMember(self, memberName):
        self.memberCount += 1
        self.members.append(memberName)

    def newBook(self, bookName):
        self.totalBookCount += 1
        self.books.append(bookName)

    def lendBook(self, bookName):
        self.borrowedBooksCount += 1
        self.currentBookCount -= 1
        self.borrowedBookName.append(bookName)

    def returnBorrowedBook(self, bookName):
        self.borrowedBooksCount -= 1
        self.currentBookCount += 1
        self.borrowedBookName.remove(bookName)
