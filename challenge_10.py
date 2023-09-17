# Given an array of strings, return the count of the number of strings with the given length.

# wordsCount(["a", "bb", "b", "ccc"], 1) → 2
# wordsCount(["a", "bb", "b", "ccc"], 3) → 1
# wordsCount(["a", "bb", "b", "ccc"], 4) → 0


def words_count(the_list, given_length):
    my_len = len(the_list) # check the length of the list and store it at variable my_len
    sum = 0
    
    for i in range(my_len): # run the loop starting from 0 to my_len
        index_value = the_list[i] # value at position i
        
        if len(index_value) == given_length:
            sum = sum + 1 # counter
        
    return print(sum)

words_count(["a", "bb", "b", "ccc"], 1)


# Given a list of numbers, find the sum of even numbers within the list
# sum_even([2, 3, 4, 5]) -> 6
# sum_even([3 ,5, 7]) -> 0

# STEPS:
# print my list
# loop through the list and print individual values
# Check if the value == even number
# if number is even add to a variable
# if not skip
# print the sum of even numbers

# def sum_even():
#     my_list = [3 ,5, 7]
#     sum = 0
    
#     for i in range(len(my_list)): # loop through the list
#         if my_list[i]%2 == 0: # Check if the value == even number
#             sum = sum + my_list[i]
            
#     return print(f'the sum of even number in the list is:{sum}')

# sum_even()