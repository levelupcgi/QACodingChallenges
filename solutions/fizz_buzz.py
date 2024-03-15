# write the python function to print the followings, constraints for input numbers from 1 to 100
# - If a number is divisible by 3 print Fizz
# - If a number is divisible by 5 print Buzz
# - If a number is divisible by both 3 and 5 print FizzBuzz

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# This function iterates through numbers from 1 to n, checks each number for divisibility by 3, 5, or both,
# and prints the appropriate response according to the rules given.
# The example provided demonstrates the output for numbers 1 to 15.

# Example usage
fizz_buzz(15)  # This will print the FizzBuzz sequence for numbers from 1 to 15
