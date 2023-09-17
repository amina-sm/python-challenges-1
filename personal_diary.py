#Personal diary

name=input("Enter your name:")# allow user to enter their names
print(name)

#writing an entry
try:
    file_name=f"{name}_diary.txt"
# personal_diary=open('Amina Diary.txt',"w")

    file_name.write("This is my personal information \n") 
    file_name.write("my name is Amina Mayengo\n")
    file_name.write("I'm persuading bachelor of electronics and telecommunication engineering fourth year\n")
    file_name.close()
except ValueError:
        print("Invalid input.")
    
# subject - file operations in python and error handling
# enter their name
# allow user to write entry
# save to a file with their name
# implement error handling