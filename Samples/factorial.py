# Write a program to calculate the factorial of a number?
# with loop, with recursion
# Let’s see a program for factorial use recursion and for-loop by handling
# negative numbers and returning a fixed value of say -9999 for negative numbers
# which should be handled in the program calling the factorial function.

def factorial(n):
    fact = 1
    if n < 0:
        print('no factorial for negative num')
    elif n ==0:
        print('fact of 0 is 1')
    else:
        for i in range(1, n+1):
            fact = fact * i
        print(f'factorial: {fact}')

# Python program to find the factorial of a number provided by the user
# using recursion


def factorial_recursion(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return x * factorial_recursion(x - 1)


