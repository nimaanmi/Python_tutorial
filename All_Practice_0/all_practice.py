# 1. Write a function to multiply 2 numbers without using multiplication.

def multiplication(x, y):
    ans = 0
    while y != 0:
        y = y - 1
        ans = ans + x
    return ans


print(multiplication(3, 2))

Output:
6
########################################################################################
# 2. 
