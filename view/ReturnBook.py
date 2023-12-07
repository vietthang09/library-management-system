import customtkinter
from tkinter.messagebox import showerror, showinfo, askyesno
import datetime

# models
from models.FineDetails import FineDetails

# controllers
from controllers.IssuedBookController import IssuedBookController
from controllers.StudentController import StudentController
from controllers.BookController import BookController
from controllers.FineDetailsController import FineDetailsController

issued_book_controller = IssuedBookController("assets/data/issued_book.csv")
students_controller = StudentController("assets/data/students.csv")
books_controller = BookController("assets/data/books.csv")
fine_details_controller = FineDetailsController("assets/data/fine_details.csv")

class ReturnBook(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(400,250)
        self.maxsize(400,250)
        self.geometry('400x250')
        self.charge_per_day = 5000
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Return Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        book_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Book ID",font=customtkinter.CTkFont(family="Verdana",size=16, weight="normal"))
        book_id_lbel.pack(pady=10)
        
        self.book_id_var = customtkinter.StringVar(self)
        self.book_id_input = customtkinter.CTkEntry(master=main_frame, width=200, textvariable=self.book_id_var)
        self.book_id_input.pack(padx=5, pady=5)
        
        return_book_btn = customtkinter.CTkButton(master=main_frame,text="Return Book",command=self.return_book)
        return_book_btn.pack(padx=10,pady=5)
    
    def return_book(self):
        book_id = self.book_id_var.get()
        book_id = int(book_id)
        
        if book_id in self.all_book_id():
            status = 'issued'
            if status in books_controller.select_book_status(book_id):
                book_detl = issued_book_controller.select_issued_book_det(book_id)
                std_exp_dt = datetime.datetime.strptime(book_detl.expired_on, "%Y-%m-%d %H:%M:%S")
                if std_exp_dt < datetime.datetime.now():
                    fine = self.total_fine(std_exp_dt)
                    conf = askyesno(title="Fine Confirmation",message=f"Student is fined, {fine[0]} VNĐ for {fine[1]} days extra. Is Student submitted fine?")
                    if conf:
                        self.save_fine_details(book_detl.book_id,book_detl.issued_to,book_detl.issued_on,fine)
                        self.return_book_func(book_id)
                    else:
                        misl_conf = askyesno(title="Miscellaneous", message="Do you want to put this book in Miscellaneous type?")
                        if misl_conf:
                            try:
                                books_controller.update_book_status(book_id,'miscellaneous')
                                issued_book_controller.move_to_miscellaneous(book_id)
                                showinfo(title='Success',message='Successfully moved in miscellaneous section.')
                            except:
                                showerror(title='Server Error',message='Something went wrong. Try Again!')
                        else:
                            showerror(title="Error - fine",message="Please take the fine!")
                else:
                    self.return_book_func(book_id)
                
            else:
                showerror(title="Not Issued",message="Given book is not issued to anyone.")
        else:
            showerror(title="Not Found", message="No any book with given id.")
    
    def all_book_id(self):
        all_bookID = books_controller.all_book_id()
        return all_bookID
    
    def return_book_func(self,book_id):
        issued_book_controller.return_book(book_id)
        books_controller.update_book_status(book_id,"available")
        showinfo(title="Book Returned",message=f"Book ID: {book_id}, returned to library successfully!")
    
    def total_fine(self,exp_dt):
        delta = datetime.datetime.now() - exp_dt
        total_fine = delta.days * self.charge_per_day
        return (total_fine, delta.days)
    
    def save_fine_details(self,book_id,student_id,issued_dt,fine):
        dt = datetime.datetime.now()
        std_dt = dt.isoformat(' ', 'seconds')
        fine_details = FineDetails(
            book_id,
            student_id,
            issued_dt,
            std_dt,
            fine[0],
            fine[1]
        )
        fine_details_controller.save_fine_detail(fine_details)
    