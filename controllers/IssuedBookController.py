import pandas as pd

from models.Book import Book
from models.IssuedBook import IssuedBook

class IssuedBookController:
    def __init__(self, file_path): 
        self.file_path = file_path
    
    def issue_book(self,issued_book):
        data = {
            "book_id": [issued_book.book_id],
            "issued_to": [issued_book.issued_to],
            "issued_on": [issued_book.issued_on],
            "expired_on": [issued_book.expired_on],
            "is_miscellaneous": [issued_book.is_miscellaneous],
        }
        df = pd.DataFrame(data)
        df.to_csv(self.file_path, mode='a', index=False, header=False)

    def select_issued_book_det(self,book_id):
        df = pd.read_csv(self.file_path)
        issued_book_data = df[df["book_id"] == book_id].iloc[0]

        book_id = issued_book_data['book_id']
        issued_to = issued_book_data['issued_to']
        issued_on = issued_book_data['issued_on']
        expired_on = issued_book_data['expired_on']
        is_miscellaneous = issued_book_data['is_miscellaneous']

        return IssuedBook(book_id, issued_to, issued_on, expired_on, is_miscellaneous)
    
    def return_book(self, book_id):
        df = pd.read_csv(self.file_path)
        line_index = df[df['book_id'] == book_id].index[0]
        df.drop(line_index, inplace=True)
        df.to_csv(self.file_path, index=False)

    def move_to_miscellaneous(self, book_id):
        df = pd.read_csv(self.file_path)
        df.loc[df["book_id"] == book_id, "is_miscellaneous"] = 1
        df.to_csv(self.file_path, index=False)

    def print_issued_books(self):
        issued_books = pd.read_csv(self.file_path)
        return issued_books

