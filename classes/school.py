from cmd import PROMPT
from urllib import response
from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
        
    def all_studs(self):
        for idx,stud in enumerate(self.students):
            print(f"{idx+1}. {stud.name}, {stud.school_id}")
            
    def find_stud_id(self, school_id):
        for stud in self.students:
            if school_id == stud.school_id:
                print(f"{stud.name}")
                print('---------------')
                print(f"age:{stud.age}")
                print(f"id:{stud.school_id}")
        
