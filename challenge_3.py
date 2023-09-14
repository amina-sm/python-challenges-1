def sum_double():
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    if a==b:
        return print(f"Double the sum of {a} and {b} is {2*(a+b)}")
        # return print("Double the sum of", a, "and", b, "is", 2*(a+b))
    else:
        #return print("Sum of two different numbers:",a, "and",b,"is", a+b)
        return print(f"Sum of two different numbers{a} and {b} is {a+b}")
    
sum_double()   

# long form
# def sum(a, b):2
#     c = a + b
#     return print(c)
# sum(2,2)

# Shorthand format
# def sum(a, b): c = a + b; return print(c)
# sum(2, 2)


# # Initiating the function to sum numbers
# def sum(a, b):
#     c = a + b
#     return print(c)

# # Take input from the user
# a =  int(input('Enter first number:'))
# b = int(input('Enter second number:'))

# # Function call & passing the arguments
# sum(a, b)



# # Initialize the function to sum numbers
# def sum():
#     a = int(input('Enter first number:')) #User inputs first number
#     b = int(input('Enter second number:')) #User inputs second number
#     c = a + b # find sum and store in c
#     return print(c) # return and print the value of c

# # Function call
# sum(2, 2) # calling the function


