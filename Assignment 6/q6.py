#Question 6
#Student Data

def student_data(student_id,**kwargs):
    print("Student ID=",student_id)
    if "student_name" in kwargs:
        print("Student Name=",kwargs["student_name"])
    if "student_class" in kwargs:
        print("Student Class=",kwargs["student_class"])

student_data(student_id="21102060")
student_data(student_id="21102060",student_name="Rahul Rana")
student_data(student_id="21102060",student_name="Rahul Rana",student_class="1st Year")
print()
