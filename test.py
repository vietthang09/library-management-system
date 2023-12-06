
from controllers.IssuedBookController import IssuedBookController
controller = IssuedBookController("assets/data/issued_book.csv")
print(controller.select_issued_book_det(1))