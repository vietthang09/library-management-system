import pandas as pd

from models.Book import Book
from models.IssuedBook import IssuedBook

class FineDetailsController:
    def __init__(self, file_path): 
        self.file_path = file_path
    
    def save_fine_detail(self, fine_details):
        data = {
            "book_id": [fine_details.book_id],
            "student_id": [fine_details.student_id],
            "returned_date": [fine_details.returned_date],
            "total_fine": [fine_details.total_fine],
            "no_of_day": [fine_details.no_of_day],
        }
        df = pd.DataFrame(data)
        df.to_csv(self.file_path, mode='a', index=False, header=False)