# Write a program to check whether a given string has balanced parentheses?
def check_balance(str1):
    count = 0
    ans = False
    for i in str1:
        if i == "(" or i == "{" or i == "[":
            count += 1
        elif i == ")" or i == "}" or i == "]":
            count -= 1
        if count < 0:
            return ans
    if count == 0:
        return not ans
    return ans


str1 = input("Enter a string of brackets: ")
print("Given string is balanced :", check_balance(str1))

'''
Explanation -
In the above code, we have initialized a count variable with zero. In if condition, if there are open brackets in the 
given string, increase the value by one, and if there are closing brackets corresponding in the open bracket, decrease 
the value by one. Finally, we checked if the count's value is equal to zero return True otherwise, False.
'''

###

'''
Approach - 3: Using Stack
The stack is a linear data structure that stores data in the LIFO (Last in First Out) manner. We traverse the string and push the open brackets inside the stack. We keep doing this process until all the opening brackets are pushed inside the stack and move the pointer forward.

When the pointer reaches the closing bracket, check the top of the stack if the corresponding to opening bracket. If matches pop the opening brackets from the stack, keep repeating until the pointer visits each closing bracket.

If all elements popped out from the bracket, it means the given string contains the valid parenthesis, and if there is any single bracket left out in the bracket, then the given string is not balanced.
'''

def check_balance2(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:

            # Here we check if the current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ")":
                    return False
            if curr_char == '{':
                if char != "}":
                    return False
            if curr_char == '[':
                if char != "]":
                    return False

                    # Here we check empty stack
    if stack:
        return False
    return True


expr = "{[()]}"

if check_balance(expr):
    print("The given string is balanced")
else:
    print("The given string is not balanced")

'''
Time Complexity
The time complexity of checking the parenthesis bracket is an optimal O(n). Here n is the total number of brackets in
 string. The searching of brackets in the given string will be linear every time since the space complexity is 0(n) 
 as we need a stack of size 'n' to store the character of the expression.
'''