def read_from_index(filename,index):
    try:
        file = open(filename, 'r')

        file.seek(index)

        print(f"\n Reading file from the index {index}:\n")

        while True:
            char = file.read(1)
            if not char:
                break
            print(char,end="")
        
        file.close()
    
    except FileNotFoundError:
        print("File is not found, please check the filename or path")
    except IOError:
        print("An Error occured while reading the file")
    except ValueError:
        print("Invalid index value.")

filename = input("Enter the filename or path:").strip()
index = int(input("Enter the index to seek and read from:"))
read_from_index(filename,index)
