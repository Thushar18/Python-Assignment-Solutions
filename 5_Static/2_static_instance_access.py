class Student:
    school_name  = "Bright Techno Schools"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def show_details(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("College:",Student.school_name)

s1 = Student("Raghav",18)
s2 = Student("Hanish",27)

s1.show_details()
s2.show_details()

print("Accessing Static variable directly through instance")
print("s1 school:",s1.school_name)
print("s2 school:",s2.school_name)

