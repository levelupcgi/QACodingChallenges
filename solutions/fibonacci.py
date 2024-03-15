# The Fibonacci. It is a series of numbers where the next number is the sum of the previous two numbers.
# The first two numbers of the Fibonacci is 0 followed by 1. Write a method that will accept one int number n.
# The method will print n number of Fibonacci numbers.

def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        # Update the values of a and b
        a, b = b, a + b


# This method starts with the first two Fibonacci numbers, 0 and 1, and iteratively calculates the next number
# by summing up the previous two. It prints n numbers from the Fibonacci sequence.
# The example provided prints the first 10 numbers of the sequence

# Example usage
fibonacci(10)  # This should print the first 10 Fibonacci numbers
