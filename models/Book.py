class Book:
    def __init__(self, book_id, title, author, edition, price, purchase_date, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.edition = edition
        self.price = price
        self.purchase_date = purchase_date
        self.status = status

    @staticmethod
    def from_dict(book_dict):
        return Book(
            book_dict['book_id'],
            book_dict['title'],
            book_dict['author'],
            book_dict['edition'],
            book_dict['price'],
            book_dict['purchase_date'],
            book_dict['status']
        )
    
    def __str__(self):
        return f"{self.book_id},{self.title},{self.author},{self.edition},{self.purchase_date},{self.price},{self.status}"