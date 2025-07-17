class Student:
    def __init__(self,name,roll_no,branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        print("Student object created with attributes.")

    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Branch: {self.branch}")
        print("-" * 30)

def main():

    student1 = Student("Rushi",401,"ECE")
    student2 = Student("Uday",553,"CSE")

    print("Student1 Info:")
    student1.display_info()

    print("Student2 Info:")
    student2.display_info()

main()



