class Animal:
    def __init__(self):
        self._type = "Tiger"
    
    def _speak(self):
        print("Roar! (from protected method)")