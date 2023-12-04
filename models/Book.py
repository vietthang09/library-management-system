class Book:
    def __init__(self, book_id, title, author, edition, price, purchase_date, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.edition = edition
        self.price = price
        self.purchase_date = purchase_date
        self.status = status
    
    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_edition(self):
        return self.edition

    def get_purchase_date(self):
        return self.purchase_date

    def get_price(self):
        return self.price

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
    def __str__(self):
        return f"{self.book_id},{self.title},{self.author},{self.edition},{self.purchase_date},{self.price},{self.status}"