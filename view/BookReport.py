import tkinter
import customtkinter
from tkinter.messagebox import showerror, showinfo
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# controllers
from controllers.BookController import BookController
from controllers.FineDetailsController import FineDetailsController
from controllers.IssuedBookController import IssuedBookController
from controllers.StudentController import StudentController

books_controller = BookController("assets/data/books.csv")
fine_details_controller = FineDetailsController("assets/data/fine_details.csv")
issued_book_controller = IssuedBookController("assets/data/issued_book.csv")
student_controller = StudentController("assets/data/students.csv")

class BookReport(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(400,450)
        # self.maxsize(400,300)
        self.geometry('400x300')
    
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Generate Book Report",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        avlb_book_export_btn = customtkinter.CTkButton(master=main_frame,text="Export Available Book",command=self.export_available_book)
        avlb_book_export_btn.pack(padx=10,pady=10)
        
        issue_book_exp_btn = customtkinter.CTkButton(master=main_frame,text="Export Issued Book",command=self.export_issued_book)
        issue_book_exp_btn.pack(padx=10,pady=10)
        
        export_all_book_btn = customtkinter.CTkButton(master=main_frame,text="Export All Book",command=self.export_all_book)
        export_all_book_btn.pack(padx=10,pady=10)
        
        export_fine_btn = customtkinter.CTkButton(master=main_frame,text="Export Fine Details",command=self.export_fine_detail)
        export_fine_btn.pack(padx=10,pady=10)
        
        # New buttons for charts
        pie_chart_btn = customtkinter.CTkButton(master=main_frame,text="Show Pie Chart",command=self.draw_pie_chart)
        pie_chart_btn.pack(padx=10,pady=10)
        
        bar_chart_btn = customtkinter.CTkButton(master=main_frame,text="Show Bar Chart",command=self.draw_bar_chart)
        bar_chart_btn.pack(padx=10,pady=10)
        
        
    def export_available_book(self):
        data = books_controller.all_available_book()
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/available_books.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")
    
    def export_issued_book(self):
        data = books_controller.all_issued_book()
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/issued_books.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")
    
    def export_all_book(self):
        data = books_controller.all_books()
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/all_books.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")
    
    def export_fine_detail(self):
        data = fine_details_controller.fine_detail()
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/fine_details.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")
    
    # New functions for drawing charts
    def draw_pie_chart(self):
        # Get data
        data = books_controller.all_status_book()
        book_status_counts = data.value_counts()  # Change this line
        print(book_status_counts)
        plt.figure(figsize=(6, 6))
        plt.pie(book_status_counts, labels=book_status_counts.index, autopct='%1.1f%%')
        plt.title('Rate of books by status')
        plt.show()

    def draw_bar_chart(self):
        data = issued_book_controller.print_issued_books()
        data['issued_on'] = pd.to_datetime(data['issued_on']).dt.date
        daily_issued_books = data['issued_on'].value_counts().sort_index()
        plt.figure(figsize=(10, 6))
        plt.bar(daily_issued_books.index, daily_issued_books)
        plt.title('Number of books borrowed per day')
        plt.xlabel('Date')
        plt.ylabel('Number of books')
        plt.show()
    
    def draw_line_chart(self):
        # Get data
        data = fine_details_controller.fine_detail()
        # Draw chart
        plt.figure(figsize=(5,5))
        plt.plot(data['book_id'], data['total_fine'])
        plt.title('Line Chart')
        plt.show()
