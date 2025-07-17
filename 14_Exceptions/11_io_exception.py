def generate_io_exception():
    print("Trying to open a directory as a file...")

    file = open(".","r")
    data = file.read()
    file.close()

def main():
    generate_io_exception()

main()
