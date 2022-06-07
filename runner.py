from tokenize import String
from classes.school import School

school = School('Ridgemont High')



#runner.py
menu="\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n"
res=input(f"{menu}")

while res !='5':
    if res=='1':
        school.all_studs()
        print(res)
    elif res=='2':
        stud_id=input('Enter students ID')
        student=school.find_stud_id(stud_id) 
        res=input(menu)  


