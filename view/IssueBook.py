import customtkinter
from tkinter.messagebox import showerror, showinfo
import datetime

# models
from models.IssuedBook import IssuedBook

# controllers
from controllers.IssuedBookController import IssuedBookController
from controllers.StudentController import StudentController
from controllers.BookController import BookController

issued_book_controller = IssuedBookController("assets/data/issued_book.csv")
students_controller = StudentController("assets/data/students.csv")
books_controller = BookController("assets/data/books.csv")

class IssueBook(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(400,250)
        self.maxsize(400,250)
        self.geometry('300x250')
        self.no_expiry_days = 5
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        self.label = customtkinter.CTkLabel(master=heading_frame, text="Issue Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        self.label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
        book_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Book ID")
        book_id_lbel.grid(column=1,row=0,padx=5, pady=5)
        
        self.book_id_var = customtkinter.StringVar(self)
        self.book_id_input = customtkinter.CTkEntry(master=main_frame, width=200,textvariable=self.book_id_var)
        self.book_id_input.grid(column=2,row=0,padx=5, pady=10)
        
        student_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Student ID")
        student_id_lbel.grid(column=1,row=1,padx=5, pady=5)
        self.student_id_var = customtkinter.StringVar(self)
        self.student_id_input = customtkinter.CTkEntry(master=main_frame, width=200, textvariable=self.student_id_var)
        self.student_id_input.grid(column=2,row=1,padx=5, pady=5)
        
        issue_book_btn = customtkinter.CTkButton(master=main_frame,text="Issue Book",command=self.issue_book)
        issue_book_btn.grid(column=2,row=2,padx=10,pady=5)
    
    def issue_book(self):
        book_id = self.book_id_var.get()
        book_id = int(book_id)
        student_id = self.student_id_var.get()
        if book_id in self.all_book_id() and student_id in self.all_student_id():
            status = 'available'
            if status in books_controller.select_book_status(book_id):
                cur_dt = datetime.datetime.now()
                std_cur_dt = cur_dt.isoformat(' ', 'seconds')
                issued_book = IssuedBook(book_id, student_id, std_cur_dt, self.expiry_datetime(), 0)
                issued_book_controller.issue_book(issued_book)
                books_controller.update_book_status(book_id,"issued")
                showinfo(title="Issued",message=f"Book issued successfully to {student_id}")
            else:
                showerror(title="Not Available",message="This book is not available or it is issued to another one.")
        else:
            showerror(title="Not Found",message="Book not found! or Student Not found! Please Check Book ID or Student ID and try again...")
        
    def all_book_id(self):
        all_bookID = books_controller.all_book_id()
        return all_bookID
    
    def all_student_id(self):
        all_studentID = students_controller.all_student_id()
        return all_studentID
    
    def expiry_datetime(self):
        exp_datetime = datetime.datetime.now()
        exp_datetime += datetime.timedelta(days=self.no_expiry_days)
        std_exp_dt = exp_datetime.isoformat(' ', 'seconds')
        return std_exp_dt
