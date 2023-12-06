import pandas as pd
import openpyxl

# models
from models.Student import Student

class StudentController:
    def __init__(self, file_path): 
        self.file_path = file_path

    def add_new_student(self, xl_file):
        with open(self.file_path, "r+") as f:
            f.truncate(0)
        try:
            wb = openpyxl.load_workbook(xl_file)
            sheet = wb['Sheet1']
            first = True
            for row in sheet.rows:
                dt = [cell.value for cell in row]
                data = {
                    "id": [dt[0]],
                    "name": [dt[1]],
                    "grade": [dt[2]],
                }
                df = pd.DataFrame(data)
                if first:
                    df.to_csv(self.file_path, mode='a', index=False, header=["id", "name", "grade"])
                    first = False
                else:
                    df.to_csv(self.file_path, mode='a', index=False, header=False)
                    
        except pd.errors.DataError as e:
            print(f"STUDENT_CONTROLLER: {e}")
            return False
        return True

    def all_student_id(self):
        df = pd.read_csv(self.file_path)
        student_ids = df.iloc[:,0].tolist()
        student_ids_str = [f"{id}" for id in student_ids]
        return student_ids_str