class Person:
    def  __init__(self):
        self.name = "Prudhvi"
        self.age = 23

def simulate_no_such_field():
    person = Person()

    print("Trying to access a non-existent field: 'gender'")
    print(person.gender)

simulate_no_such_field()