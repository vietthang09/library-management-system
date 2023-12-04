import openpyxl
import pandas as pd

class LMS:
    def add_new_book(self, data):
        with open('books.txt', 'a') as f:
            new_book_data = data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "," + data[4] + "," + data[5] + ",available" + '\n'
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
    
    def select_book_status(self,book_id):
        with open('books.txt', 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip().split(',')[0] == str(book_id):
                return line.strip().split(',')[6]
    
    def select_book_detail(self,book_id):
        with open('books.txt', 'r') as f:
            for line in f:
                data = line.strip().split(',')
                if data[0] == str(book_id):
                    return data

    
    def update_book_details(self,book_id, data):
        with open('books.txt', 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip().split(',')[0] == str(book_id):
                lines[i] = data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "," + data[4] + "," + data[5] + "," + '\n'
                break

        with open('books.txt', 'w') as f:
            f.writelines(lines)