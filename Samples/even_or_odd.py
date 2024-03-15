# Write a method that will accept one int as an argument.
# The method prints Even if the number is even and Odd if the number is odd.

def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


# This method uses the modulo operator (%) to determine if the number is divisible by 2. If the remainder is 0,
# it prints "Even"; otherwise, it prints "Odd".
# The example usage correctly demonstrates the method with both an odd and an even number.

# Example usage
check_even_odd(5)  # This should print "Odd"
check_even_odd(4)  # This should print "Even"
