from package_a.car import Car

class TestCar:
    def show(self):
        car = Car()
        print("Accessing public fields from another package:")
        print(car.brand)
        print(car.speed)
        car.display_info()
