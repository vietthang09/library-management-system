import customtkinter
from controllers.BookController import BookController
from tkinter.messagebox import showerror, showinfo
controller = BookController("assets/data/books.csv")
class DeleteBook(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(400,250)
        self.maxsize(400,250)
        self.geometry('400x250')
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Delete Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        book_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Book ID", font=customtkinter.CTkFont(family="Verdana",size=18))
        book_id_lbel.pack()
        
        self.book_id_input = customtkinter.CTkEntry(master=main_frame, width=200)
        self.book_id_input.pack(padx=5, pady=10)
        
        delete_book_btn = customtkinter.CTkButton(master=main_frame,text="Delete Book",command=self.delete_book)
        delete_book_btn.pack(padx=10,pady=10)
    
    def delete_book(self):
        id_lists = controller.all_book_id()
        if int(self.book_id_input.get()) in id_lists:
            controller.delete_book(int(self.book_id_input.get()))
            showinfo(title="Deleted",message=f"Book ID : {self.book_id_input.get()}, deleted successfully.")
        else:
            showerror(title="Not Found",message="Book not found")