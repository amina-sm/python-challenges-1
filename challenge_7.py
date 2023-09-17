

# Given an array of ints, we'll say that a triple is a value appearing 3 times in a row in the array. Return true if the array does not contain any triples.

# noTriples([1, 1, 2, 2, 1]) → true
# noTriples([1, 1, 2, 2, 2, 1]) → false
# noTriples([1, 1, 1, 2, 2, 2, 1]) → false

# indexes in python
import time

def noTriples(a):
    for i in range(len(a) - 2):
        print(f'Checking {a[i]} {a[i+1]} {a[i+2]}:')
        if a[i] == a[i+1] and a[i+1] == a[i+2]:
            print(False)
        else: print(True)

noTriples([1, 1, 2, 2, 1]) # len = 5
noTriples([1, 1, 2, 2, 2, 1])
noTriples([1, 1, 1, 2, 2, 2, 1])
noTriples([0, 1, 2, 3, 3, 3, 4,2,1])

