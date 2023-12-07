import pandas as pd

from models.Book import Book

class BookController:
    def __init__(self, file_path): 
        self.file_path = file_path

    def add_new_book(self, book):
        try:
            data = {
                "book_id": [book.book_id],
                "title": [book.title],
                "author": [book.author],
                "edition": [book.edition],
                "price": [book.price],
                "purchase_date": [book.purchase_date],
                "status": [book.status]
            }
            df = pd.DataFrame(data)
            df.to_csv(self.file_path, mode='a', index=False, header=False)
        except pd.errors.DataError as e:
            print(f"BOOK_CONTROLLER: {e}")
    
    def view_book_list(self):
        books = []
        try:
            df = pd.read_csv(self.file_path)
            book_dicts = df.to_dict(orient='records')
            books = [Book.from_dict(book_dict) for book_dict in book_dicts]
        except pd.errors.DataError as e:
            print(f"BOOK_CONTROLLER: {e}")
        return books
    
    def update_book_details(self,updated_book):
        df = pd.read_csv(self.file_path)
        line_index = df[df["book_id"] == updated_book.book_id].index[0]
        df.loc[line_index] = [updated_book.book_id, updated_book.title, updated_book.author, updated_book.edition, updated_book.price, updated_book.purchase_date, updated_book.status]
        df.to_csv(self.file_path, index=False)

    def delete_book(self, book_id):
        df = pd.read_csv(self.file_path)
        line_index = df[df['book_id'] == book_id].index[0]
        df.drop(line_index, inplace=True)
        df.to_csv(self.file_path, index=False)
    
    def select_book_detail(self,id):
        df = pd.read_csv(self.file_path)
        book_data = df[df["book_id"] == id].iloc[0]

        book_id = book_data['book_id']
        title = book_data['title']
        author = book_data['author']
        edition = book_data['edition']
        price = book_data['price']
        purchase_date = book_data['purchase_date']
        status = book_data['status']
        return Book(book_id, title, author, edition, price, purchase_date, status)
    
    def all_book_id(self):
        df = pd.read_csv(self.file_path)
        book_ids = df.iloc[:,0].tolist()
        return book_ids

    def select_book_status(self,book_id):
        df = pd.read_csv(self.file_path)
        book_status = df[df["book_id"] == book_id]["status"].values[0]
        return book_status
    

    def update_book_status(self,book_id,status):
        df = pd.read_csv(self.file_path)
        df.loc[df["book_id"] == book_id, "status"] = status
        df.to_csv(self.file_path, index=False)

    def all_available_book(self):
        df = pd.read_csv(self.file_path)
        available_books = df[df["status"] == "available"]
        return available_books

    def all_issued_book(self):
        df = pd.read_csv(self.file_path)
        issued_books = df[df["status"] == "issued"]
        return issued_books
    
    def all_status_book(self):
        df = pd.read_csv(self.file_path)
        all_status = df["status"]
        return all_status

    
    def all_books(self):
        df = pd.read_csv(self.file_path)
        books = df[df["status"] == "issued" or "available"]
        return books
    
    def miscellaneous_books(self):
        books = []
        df = pd.read_csv(self.file_path)
        miscellaneous_books = df[df["status"] == "miscellaneous"].values
        for book in miscellaneous_books:
            book_id = book[0]
            title = book[1]
            author = book[2]
            edition = book[3]
            price = book[4]
            purchase_date = book[5]
            status = book[6]
            _book = Book(book_id, title, author, edition, price, purchase_date, status)
            books.append(_book)
        return books
        
    
    

    