def read_text_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8', errors='ignore')
        print("File Contents:")

        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("File was not Found")
    except IOError:
        print("An Error occured while reading the file")

filename = input("Enter the file name or path:")
read_text_file(filename)