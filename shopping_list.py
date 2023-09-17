# def  main():
#     shopping_list=[]
    
#     while True:
#         print("Enter 1 for adding item in a list:")
#         print("Enter 2 for viewing item in a list")
#         print("Enter 3 for saving item in a file")
#         print("Enter 4 for finishing a program")
#         choice=input("enter 1/2/3/4")
        
#         if choice=="1":
#             try:
#                 shopping_item=input("Enter your item:")
#                 quantity=int(input("Enter your item quantity"))
#                 shopping_list.append((shopping_item,quantity))
#                 print(f'shopping item is {shopping_item} and its quantity is {quantity}')
#             except:ValueError
#             print("invalid input please enter correct quantity")
    
#         elif choice=="2":
#             print("Shopping list:")
#             for i, (shopping_item,quantity)in  enumerate (shopping_list, start=1):
#                 print(f'{i} {shopping_item} {(quantity)}')
                
#         elif choice=="3":
#               save_shopping_list(shopping_list)

#         elif choice == '4':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a valid option (1/2/3/4).")

# def save_shopping_list(shopping_list):
#     try:
#         file_name = input("Enter the file name to save the list: ")
#         with open(file_name, 'w') as file:
#             for item_name, quantity in shopping_list:
#                 file.write(f"{item_name} ({quantity})\n")
#         print(f"Shopping list saved to {file_name}.")
#     except Exception as e:
#         print(f"Error saving the list: {str(e)}")

# if __name__ == "__main__":
#     main()


def main():
    shopping_list = []
    
    while True:
        print("Shopping List Application")
        print("1. Add item")
        print("2. View list")
        print("3. Save list to file")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            try:
                item_name = input("Enter the item's name: ")
                quantity = int(input("Enter the quantity: "))
                shopping_list.append((item_name, quantity))
                print(f"{item_name} ({quantity}) added to the list.")
            except ValueError:
                print("Invalid input. Please enter a valid quantity (an integer).")
        elif choice == '2':
            print("Shopping List:")
            for i, (item_name, quantity) in enumerate(shopping_list, start=1):
                print(f"{i}. {item_name} ({quantity})")
        elif choice == '3':
            save_shopping_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

def save_shopping_list(shopping_list):
    try:
        file_name = input("Enter the file name to save the list: ")
        with open(file_name, 'w') as file:
            for item_name, quantity in shopping_list:
                file.write(f"{item_name} ({quantity})\n")
        print(f"Shopping list saved to {file_name}.")
    except Exception as e:
        print(f"Error saving the list: {str(e)}")

if __name__ == "__main__":
    main()





        