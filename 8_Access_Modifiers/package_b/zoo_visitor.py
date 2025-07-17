from package_a.animal import Animal

class Visitor:
    def visit(self):
        animal = Animal()
        print("Visitor accessing private field:",animal._type)
        animal._speak()