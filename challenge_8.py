# Given a string, return true if the first instance of "x" in the string is immediately followed by another "x".

# doubleX("axxbb") → true
# doubleX("axaxax") → false
# doubleX("xxxxx") → true

# def doubleX(a):
#     for i in range(len(a) -1):
#         # print(f'checking if {a[i]} equal to {a[i]}')
#         if a[i] =='x' and  a[i+1]=='x':
#             return True
#     return False    
#         #     print(True)
#         # else: print(False)
# doubleX('axxxbnnx')


def has_double_x(string):
    for i in range(len(string) - 1):
        if string[i] == 'x' and string[i+1] == 'x':
            return True
    return False

# Test cases

print(has_double_x("xoxo"))  # True, 'x' is followed by 'x'
# print(has_double_x("xyxy"))  # False, 'x' is not followed by 'x'
# print(has_double_x("xxxx"))  # True, multiple consecutive 'x's
# print(has_double_x("abc"))   # False, no 'x'

        
        
        
        
        
# if a[i] == a[i+1] and a[i+1] == a[i+2]:
#             print(False)
#         else: print(True)