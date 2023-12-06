class FineDetails:
    def __init__(self, book_id, student_id, issued_on, returned_date, total_fine, no_of_day):
        self.book_id = book_id
        self.student_id = student_id
        self.issued_on = issued_on
        self.returned_date = returned_date
        self.total_fine = total_fine
        self.no_of_day = no_of_day
    
    def __str__(self):
        return f"{self.book_id},{self.student_id},{self.returned_date},{self.total_fine},{self.no_of_day}"