import sys

def write_to_text_file():
    try:
        print("Enter the text to write the file (type 'exit' to stop):")

        file = open("output.txt", "w")
        buffer = ""

        while True:
            char = sys.stdin.read(1)
            if char == "\n":
                if buffer.strip().lower() == "exit":
                    break
                file.write(buffer + "/n")
                buffer = ""
            else:
                buffer += char
        file.close()
        print("text written to output.txt")

    except IOError:
        print("An Error occured while writing to the file.")

write_to_text_file()

