# An anagram is when all the letters in one string exist in another but the order of letters does not matter.
# Write a method that accepts two string arguments and returns true if they are anagram and false if they are not.

def are_anagrams(str1, str2):
    # Remove spaces and make lowercase for a fair comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# This method first removes any spaces from the strings and converts them to lowercase to ensure the comparison is
# case-insensitive. Then, it checks if sorting the characters of both strings results in two identical lists, indicating
# they are anagrams. The example usage with "Listen" and "Silent" correctly returns True, showing they are anagrams

# Example usage
print(are_anagrams("Listen", "Silent"))

