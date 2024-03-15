# A palindrome is a word, phrase, number, or sequence of words that reads the same backward as forward.
# The straightforward solution would be to convert the number to a string and use the above approach.
# Some interviewers will not allow it. So let’s take a look at what we can do here.

def is_palindrome(string):
    """
    function which return reverse of a string
    Time complexity: O(n)
    Auxiliary Space: O(1)
    """
    return string == string[::-1]


def is_palindrome2(string):
    # Run loop from 0 to len/2
    end = int(len(string)/2)
    for i in range(0, end):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

a = str(45678)
b = 'kayak'
print(is_palindrome2(a))
print(is_palindrome2(b))
