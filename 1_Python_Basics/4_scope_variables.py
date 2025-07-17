value = "Global Scope"

def show_scope():
    value = "Local Scope"

    print("Inside the Function")
    print("The Local Variable is ", value)

def show_global():
    print("Outside the Function")
    print("The Global Variable is ", value)

show_scope()
show_global()
