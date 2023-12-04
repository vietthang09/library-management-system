from models.Book import Book
class BookController:
    def __init__(self, file_path): 
        self.file_path = file_path

    def add_new_book(self, book):
        with open(self.file_path, 'a') as f:
            f.write(f"{book.book_id},{book.title},{book.author},{book.edition},{book.price},{book.purchase_date},{book.status}\n")
        return True
    
    def view_book_list(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        books = []
        for line in lines:
            data = line.strip().split(',')
            book = Book(*data)
            books.append(book)
        return books
    
    def all_book_id(self):
        book_ids = []
        with open(self.file_path, 'r') as f:
            for line in f:
                book_id = line.strip().split(',')[0]
                book_ids.append(book_id)
        return book_ids

    def select_book_status(self,book_id):
        with open(self.file_path, 'r') as f:
            for line in f:
                book_data = line.strip().split(',')
                if book_data[0] == str(book_id):
                    return book_data[6]
    
    def select_book_detail(self,book_id):
        with open(self.file_path, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                if data[0] == str(book_id):
                    book = Book(*data)
                    return book

    def update_book_details(self,book_id, updated_book):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip().split(',')[0] == str(book_id):
                lines[i] = f"{updated_book.book_id},{updated_book.title},{updated_book.author},{updated_book.edition},{updated_book.price},{updated_book.purchase_date},{updated_book.status}\n"
                break

        with open(self.file_path, 'w') as f:
            f.writelines(lines)

    def delete_book(self, book_id):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip().split(',')[0] == str(book_id):
                del lines[i]
        with open(self.file_path, 'w') as f:
            f.writelines(lines)
        return "deleted"