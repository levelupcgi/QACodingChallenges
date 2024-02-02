# Write a program to swap 2 numbers without using the 3rd (temporary) variable?

def swap_nums(a, b):
    try:
        print(f'values before swapping: {a} and {b}')
        a = a + b
        b = a - b
        a = a - b
        print(f'values after swapping: {a} and {b}')
        return a, b
    except TypeError as err:
        print(f'values after swapping: {None}')
        return None


# it’s important that before submitting the solution, it’s always recommended to go through (or dry run) the code for
# at least 2-to 3 inputs. Let’s try for positive and negative values.

assert swap_nums(3, 4) == (4, 3)
assert swap_nums(-3, 4) == (4, -3)
assert swap_nums(0, 4) == (4, 0)
assert swap_nums(None, 4) is None
assert swap_nums('\n', 4) is None
