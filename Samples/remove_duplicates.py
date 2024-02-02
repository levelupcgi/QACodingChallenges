# Write a Python program for a given string S which may contain lowercase and uppercase characters.
# The task is to remove all duplicate characters from the string and find the resultant string.
#
# Note: The order of remaining characters in the output should be the same as in the original string.


# Naive Approach:
def remove_duplicates_1(string):
    """
    Iterate through the string and for each character check if that particular character has occurred before
    it in the string. If not, add the character to the result, otherwise the character is not added to result.

    Time Complexity : O(n * n)
    Auxiliary Space : O(1) , Keeps order of elements the same as input.
    """
    p = ""
    for char in string:
        if char not in p:
            p = p + char
    print(p)


# Remove duplicates from a given string using Hashing
def remove_duplicates_hash(string):
    """
    Iterating through the given string and use a map to efficiently track of encountered characters.
    If a character is encountered for the first time, it’s added to the result string, Otherwise, it’s skipped.
    This ensures the output string contains only unique characters in the same order as the input string.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # access time in unordered_map on is O(1) generally if no collisions occur
    # and therefore it helps us check if an element exists in a string in O(1)
    # time complexity with constant space.

    n = len(string)
    unique_string = {}
    index = 0

    for i in range(n):
        if string[i] not in unique_string:  # or unique_string[string[i]] == 0:
            # string[index] = string[i]
            # print(string[index], end='')
            index += 1
            unique_string[string[i]] = 1

    ans = "".join(unique_string)
    # print(string)
    # print(unique_string)
    print(ans)
    return ans


remove_duplicates_hash("leveluplevels")
print()
remove_duplicates_1("pythonpytest")
