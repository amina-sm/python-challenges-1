#def calculator():
while True:
    try:
         a=int(input('enter the first number: '))
         b=int(input('enter the second number: '))
         print("Choose 1 for addition")
         print("Choose 2 for substraction function")
         print("Choose 3 for multiplication")
         print("Choose 4 for division")
         print("Enter 5 for quit  the calculator")
        
         choice=input("enter your choice: ")
        
         if choice=="1":
            c=a+b
            print(f'The sum of {a} + {b}= {c}')
        
         elif choice=="2":
            d=a-b
            print(f'The difference between {a} - {b} = {d}')
    
         elif choice=="3":
            e=a*b
            print(f'the product of {a} * {b} = {e}')
            
         elif choice=="4":
            # f=a/b
            # print(f'the result of division of {a} / {b} = {f}') 
             if b == 0:
                print("Error: Division by zero is not allowed.")
             else:
                f = a / b
                print(f'The result of division of {a} / {b} = {f}')
            
         elif choice == "5":
            break
         else:
            print("Invalid choice. Please enter a valid option.")
    # except ZeroDivisionError:
    #     print("Error: Division by zero is not allowed.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
print("\nThank you for using the program!")

