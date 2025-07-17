def generate_file_not_found_exception():
    print("Attempting to open a non-existent file...")
    file = open("batman.txt","r")
    content = file.read()
    file.close()
    print("File content:",content)

def main():
    generate_file_not_found_exception()

main()
