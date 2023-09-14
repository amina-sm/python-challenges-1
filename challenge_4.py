def sum():
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    if a==10:
        return print('return True if a is equal to 10')
    elif b==10:
        return print('return true if b is equal to 10')
    elif a+b==10:
        return print(f'The sum of{a} and{b} equal to 10 returns True')
    else:
        return print("False")
sum()     