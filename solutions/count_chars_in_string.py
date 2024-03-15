# Write a method that accepts a string as an argument. The method counts the number of appearances of each char
# and returns a map. The key will be a letter and the value will be the number of appearances in the string.
# See the input and output in the example.

from collections import Counter


def count(string):
    # string = string.lower()   # to ignore the case
    return dict(Counter(string))


def count_loop(string):
    """
    Here, an empty dictionary is instantiated. Then, do a for loop through the string . If the key is not yet in the
    dictionary, create it with a value of 1, and if it is, add 1 to the key’s value.
    """
    counted = {}
    for char in string:
        if char not in counted:
            counted[char] = 1
        else:
            counted[char] += 1
    return counted


def count_dic(string):
    return {x: string.count(x) for x in string}


def count_get(string):
    """
    Create an empty dictionary, and loop through the list like before. The 0 in counted.get(i, 0) instructs Python to
     set it as a default value if the key doesn’t yet exist, and then the function is adding 1 to it.
    """
    counted = {}
    for char in string:
        counted[char] = counted.get(char, 0) + 1
    return counted


def count_setdefault(string):
    """
    In this situation, setdefault() does exactly the same thing as get(). It creates the key if it doesn’t exist
    with a default value of 0 and then adds 1. If it does exist, it adds 1 again.
    """
    counted = {}
    for char in string:
        counted[char] = counted.setdefault(char, 0) + 1
    return counted


print(count('BASasdf basdfcsdfASDGSd'))
# {'B': 1, 'A': 2, 'S': 3, 'a': 2, 's': 3, 'd': 4, 'f': 3, ' ': 1, 'b': 1, 'c': 1, 'D': 1, 'G': 1}
# {'b': 2, 'a': 4, 's': 6, 'd': 5, 'f': 3, ' ': 1, 'c': 1, 'g': 1}  ignored case
print(count_loop('BASasdf basdfcsdfASDGSd'))
print(count_dic('BASasdf basdfcsdfASDGSd'))
