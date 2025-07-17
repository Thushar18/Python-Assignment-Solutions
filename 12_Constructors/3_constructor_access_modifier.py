class AccessModifierDemo:
    def __init__(self):
        print("Public Constructor is called.")

    def _protected_constructor(self):
        print("Protected Constructor is called.")
    
    def __private_constructor(self):
        print("Private Constructor is called.")

    def _default_constructor(self):
        print("Default Constructor is called.")
    
    def call_private(self):
        self.__private_constructor()
    
    def call_protected(self):
        self._protected_constructor()

def main():
    obj = AccessModifierDemo()
    obj._default_constructor()

    obj.call_private()
    obj.call_protected()

main()