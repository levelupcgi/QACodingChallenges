# Prime number. A prime number is a number that can only be divided by itself and 1 without remainder.

# Program to check if a number is prime or not


def is_prime_flag(num):
    # define a flag variable
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")


def is_prime_elif(num):
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")


num = 29
# To take input from the user
# num = int(input("Enter a number: "))
is_prime_flag(num)

num = 407
# To take input from the user
# num = int(input("Enter a number: "))
is_prime_elif(num)
