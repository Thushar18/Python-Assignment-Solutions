from package_b.zoo import ZooAnimal
from package_b.zoo_visitor import Visitor
from package_b.test_car import TestCar

print("--- From Subclass from Different Package ---")
zoo_animal = ZooAnimal()
zoo_animal.access_protected()

print("--- From Non-Subclass from Different Package ---")
visitor = Visitor()
visitor.visit()

print("--- Public Fields and Method Access ---")
test = TestCar()
test.show()
