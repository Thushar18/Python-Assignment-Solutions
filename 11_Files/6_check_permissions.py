import os

def check_file_permissions(filename):
    try:
        if not os.path.exists(filename):
            print("File does not exists")
            return
        
        print(f"/n Checking Permissions for: {filename}")

        if os.access(filename,os.R_OK):
            print("Read access : Yes")
        else:
            print("Read access: No")
        
        if os.access(filename,os.W_OK):
            print("Write access: Yes")
        else:
            print("Write access: No")
    
    except Exception as e:
        print(f"Error occured: {e}")
    
filename = input("Enter filename or path:").strip()
check_file_permissions(filename)