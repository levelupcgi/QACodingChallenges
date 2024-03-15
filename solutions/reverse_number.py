#  Write a program to reverse a number?
# If the input is 345 then the output should be 543 (which is the reverse of 345)

def reverse_number(num):
    if type(num) is int and num >= 0:
        print(f"Input number {num}")
        rev_num = 0
        while num != 0:
            digit = num % 10
            rev_num = rev_num * 10 + digit
            num = num // 10
        print(f"Output : {rev_num}")
        return rev_num
    else:
        print(f'Given number is not an integer: {num}')
        return None


assert reverse_number(4567) == 7654
assert reverse_number(4567) == 7654
assert reverse_number(1) == 1
assert reverse_number(0) == 0
assert reverse_number(-1) == None
assert reverse_number(45.55) is None
assert reverse_number('a') is None
assert reverse_number('\n') is None
assert reverse_number('   ') is None

