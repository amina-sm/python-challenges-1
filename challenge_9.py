

# Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" return "Buzz". If both the "f" and "b" conditions are true, return "FizzBuzz". 
# In all other cases, return the string unchanged. (See also: FizzBuzz Code)
# fizzString("fig") → "Fizz"
#  fizzString("dib") → "Buzz"
# fizzString("fib") → "FizzBuzz"

# message = 'Python is fun'
# # check if the message starts with Python
# print(message.startswith('Python'))

# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x) 

# ------ ------ ------ ------ PEP8 ------ ------ ------ ------ ------

# https://realpython.com/python-pep8/

#  ------ ------ ------ ------ ------ ------ ------ ------ ------ ------
# naming conventions in python (PEP8)
# variables: 
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)

    #Legal variable names:
    # myvar = "John"
    # my_var = "John"
    # _my_var = "John"
    # myVar = "John"
    # MYVAR = "John"
    # myvar2 = "John"

    #Illegal variable names:
    # 2myvar = "John"
    # my-var = "John"
    # my var = "John"
    
# Function:
    # Use a lowercase word or words. Separate words by underscores to improve readability.
    # Examples: function, my_function
    
    
# ------ ------ ------ ------ OPERATORS ------ ------ ------ ------ ------

# https://www.w3schools.com/python/python_operators.asp

#  ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ -


def check_string():
    word = "fib" # something shaped like a ball
    # if word starts with f return fizz
    # if word ends with b return buzz
    if word.startswith('f') and word.endswith('b'):
        return print('FizzBuzz')
    elif word.startswith('f'):
        return print("Fizz")
    elif word.endswith('b'):
        return print("Buzz")
    else: return print(word)
        
check_string()
        

# def fizzString(s):
#     result = ""
#     length = len(s)

#     # Check for "Fizz"
#     if length > 0 and s[0] == "f":
#         result += "Fizz"

#     # Check for "Buzz"
#     if length > 0 and s[length - 1] == "b":
#         result += "Buzz"

#     # If neither "Fizz" nor "Buzz" conditions are met, keep the original string unchanged.
#     if not result:
#         result = s

#     return result

# # Test cases
# print(fizzString("fig"))  # Output: "Fizz"
# print(fizzString("dib"))  # Output: "Buzz"
# print(fizzString("fib"))  # Output: "FizzBuzz"