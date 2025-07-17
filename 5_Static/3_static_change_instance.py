class Bike:
    brand="Royal Enfield"

    def __init__(self,model):
        self.model = model
    
    def modify_brand(self,new_brand):
        self.brand = new_brand

bike1 = Bike("Classic 350")
bike2 = Bike("Bullet 350")

bike1.modify_brand("Harley-Davidson")

print("bike1 brand:",bike1.brand)
print("bike2.brand",bike2.brand)
print("Bike class brand:",Bike.brand)