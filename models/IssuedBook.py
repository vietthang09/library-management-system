class IssuedBook:
    def __init__(self, book_id, issued_to, issued_on, expired_on, is_miscellaneous):
        self.book_id = book_id
        self.issued_to = issued_to
        self.issued_on = issued_on
        self.expired_on = expired_on
        self.is_miscellaneous = is_miscellaneous
    
    def __str__(self):
        return f"{self.book_id},{self.issued_to},{self.issued_on},{self.expired_on},{self.is_miscellaneous}"