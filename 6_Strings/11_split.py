def split(str):
    result=[]
    word = ""
    for char in str:
        if char != " ":
            word += char
        else:
            if word!= "":
                result.append(word)
                word = ""

    if word != "":
        result.append(word)
    return result

input_str = input("Enter a sentence to split:")

split_words = split(input_str)

print("Split Words are:",split_words)


