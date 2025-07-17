from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.name = "Automated Vehicle"
    
    def display_type(self):
        print("This is a vehicle")
    
    @abstractmethod
    def start_engine(self):
        pass
    
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = "Car"

    def start_engine(self):
        print(f"{self.name}: Engine Started")
    
    def stop_engine(self):
        print(f"{self.name}: Engine Stopped")

    def use_methods(self):
        self.start_engine()
        self.stop_engine()

        self.display_type()

if __name__ == "__main__":
    car = Car()
    print("Calling all methods from child class instance:")
    car.use_methods()


