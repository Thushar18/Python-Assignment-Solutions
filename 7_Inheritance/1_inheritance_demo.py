class A:
    def __init__(self):
        self.value = "value from class A"
    
    def method1(self):
        print("Method1 from class A")
    
    def method2(self):
        print("Method2 from class A")
    
    def common(self):
        print("Overriden method in class A")

class B(A):
    def __init__(self):
        self.value = "value from class B"
    
    def method3(self):
        print("Method3 from class B")
    
    def method4(self):
        print("Method4 from class B")
    
    def common(self):
        print("Overridden method in class B")

class C(B):
    def __init__(self):
        self.value = "value from class C"
    
    def method5(self):
        print("Method5 from class C")
    
    def method6(self):
        print("Method6 from class C")
    
    def common(self):
        print("Overridden method in class C")

def main():
    print("--- Object of class A ---")
    a = A()
    a.method1()
    a.method2()
    a.common()
    print("Data Member:",a.value)

    print("--- Object of class B ---")
    b = B()
    b.method3()
    b.method4()
    b.common()
    print("Data Member",b.value)

    print("--- Object of class C ---")
    c= C()
    c.method5()
    c.method6()
    c.common()
    print("Data Member",c.value)

    print("--- Runtime Polymorphism ---")

    a_ref : A
    a_ref = B()
    a_ref.common()
    print("Data Member(A ref to B)", a_ref.value)

    a_ref = C()
    a_ref.common()
    print("Data Member (A ref to C)", a_ref.value)

main()


