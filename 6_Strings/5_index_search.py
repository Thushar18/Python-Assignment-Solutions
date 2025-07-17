def search_substr(main_str,sub_str):
    try:
        position = main_str.index(sub_str)
        print(f"{sub_str} found at index {position}")
    except:
        print(f"{sub_str} not found in the string")

main_str = input("Enter the main string:")
sub_str = input("Enter the substring to search:")

search_substr(main_str,sub_str)
