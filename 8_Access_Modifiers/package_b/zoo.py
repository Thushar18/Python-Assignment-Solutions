from package_a.animal import Animal

class ZooAnimal(Animal):
    def access_protected(self):
        print("From subclass (other package) - Type:", self._type)
        self._speak()