import openpyxl
import pandas as pd

class LMS:
    def add_new_book(self, data):
        with open('books.txt', 'a') as f:
            new_book_data = '\n' + data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "," + data[4] + "," + data[5] + ",available"
            f.write(new_book_data)
        return True
    
    
    def add_new_student(self, xl_file):
        wb = openpyxl.load_workbook(xl_file)
        sheet = wb['Sheet1']
        for row in sheet.rows:
            data = [cell.value for cell in row]
            new_book_data = str(data[0]) + "," + data[1] + "," + data[2] + '\n'
            with open('students.txt', 'a') as f:
                f.write(new_book_data)
        return True
    
    
    def delete_book(self, book_id):
        with open('books.txt', 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip().split(',')[0] == str(book_id):
                del lines[i]
        with open('books.txt', 'w') as f:
            f.writelines(lines)
        return "deleted"
    
    def view_book_list(self):
        with open('books.txt', 'r') as f:
            data = f.read()
            lines = data.splitlines()
        data = []
        for line in lines:
            data.append(line.strip().split(','))
        return data

    
    def miscellaneous_books(self):
        self.cur.execute("SELECT * FROM books WHERE status = 'miscellaneous'")
        return self.cur.fetchall()
    
    def view_issued_book(self,id):
        self.cur.execute("SELECT * FROM issued_book WHERE book_id = ? and is_miscellaneous = ?", (id,0))
        return self.cur.fetchone()
    
    def view_student(self,id):
        self.cur.execute("SELECT * FROM student WHERE id = ?", (id,))
        return self.cur.fetchone()
    
    def all_book_id(self):
        book_ids = []
        with open('books.txt', 'r') as f:
            for line in f:
                book_data = line.strip().split(',')
                book_id = book_data[0]
                book_ids.append(book_id)
        return book_ids
    
    def all_student_id(self):
        student_ids = []
        with open('students.txt', 'r') as f:
            for line in f:
                student_data = line.strip().split(',')
                student_id = student_data[0]
                student_ids.append(student_id)
        return student_ids
    
    def issue_book(self,data):
        sql = '''INSERT INTO issued_book (book_id,issued_to,issued_on,expired_on)
            VALUES(?,?,?,?) '''
        self.cur.execute(sql, data)
        self.conn.commit()
        return self.cur.lastrowid
    
    def delete_issued_book(self):
        try:
            sql = 'DELETE FROM issued_book'
            self.cur.execute(sql)
            self.conn.commit()
            return "deleted"
        except:
            return "error"
    
    def all_issued_book_id(self):
        self.cur.execute("SELECT book_id FROM issued_book WHERE is_miscellaneous = ?",(0,))
        return self.cur.fetchall()
    
    def return_book(self,book_id):
        try:
            sql = 'DELETE FROM issued_book WHERE book_id=?'
            self.cur.execute(sql, (book_id,))
            self.conn.commit()
            return "returned"
        except:
            return "error"
    
    def update_book_status(self,book_id,status):
        sql = '''UPDATE books SET status = ? WHERE book_id = ?'''
        self.cur.execute(sql,(status,book_id,))
        self.conn.commit()
    
    def select_book_status(self,book_id):
        with open('books.txt', 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip().split(',')[0] == str(book_id):
                return line.strip().split(',')[6]
    
    def select_issued_book_det(self,book_id):
        self.cur.execute("SELECT * FROM issued_book WHERE book_id=?", (book_id,))
        return self.cur.fetchone()
    
    def select_book_detail(self,book_id):
        with open('books.txt', 'r') as f:
            for line in f:
                data = line.strip().split(',')
                if data[0] == str(book_id):
                    return data
    
    def all_available_book(self):
        sql="SELECT book_id, book_name, book_author, book_edition, book_price FROM books WHERE status = 'available'"
        return (sql,self.conn)
    
    def all_issued_book(self):
        sql="SELECT book_id, book_name, book_author, book_edition, book_price FROM books WHERE status = 'issued'"
        return (sql,self.conn)
    
    def all_books(self):
        sql="SELECT book_id, book_name, book_author, book_edition, book_price FROM books WHERE status = 'available' or status = 'issued'"
        return (sql,self.conn)
    
    def fine_detail(self):
        sql="SELECT * FROM fine_details"
        return (sql,self.conn)
    
    def move_to_miscellaneous(self,id):
        sql = '''UPDATE issued_book SET is_miscellaneous = ? WHERE book_id = ?'''
        self.cur.execute(sql,(1,id,))
        self.conn.commit()
    
    def update_book_details(self,book_id, data):
        with open('books.txt', 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip().split(',')[0] == str(book_id):
                lines[i] = data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "," + data[4] + "," + data[5] + "," + '\n'
                break

        with open('books.txt', 'w') as f:
            f.writelines(lines)

    
    def save_fine_detail(self,data):
        sql = '''INSERT INTO fine_details(book_id,student_id,issued_on,returned_date,total_fine,no_of_day)
            VALUES(?,?,?,?,?,?)'''
        self.cur.execute(sql, data)
        self.conn.commit()
        return self.cur.lastrowid