class PrivateAccess:
    def __init__(self):
        self.private_field = "Private Data"
    
    def __private_method(self):
        print("Private Method Called")

    def access_private_inside(self):
        print("Inside class -Field:",self.private_field)
        self.__private_method

class PrivateSubClass(PrivateAccess):
    def access_private_from_subclass(self):
        try:
            print("Accessing Private Field:", self.private_field)
        
        except AttributeError:
            print("cannot access private field in subclass")
        
        try:
            self.private_method()
        except:
            print("cannot call private method in subclass")

obj = PrivateAccess()
obj.access_private_inside()

sub = PrivateSubClass()
sub.access_private_from_subclass()
