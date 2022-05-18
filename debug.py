# The lone sum of the given numbers is the sum of the given 3 numbers
# but same numbers are exclude from the sum
# so if all three numbers are same then the sum is 0
def lone_sum(a, b, c):
    # first check if all 3 numbers are the same
    if a == b and b == c:
        # if true, then return 0 as the sum
        return 0
    # if not all 3 numbers are same, then check if there are any two matches
    # if the first two numbers are same, then return the third number as the sum
    elif a == b:
        return c
    # if first & last numbers are same, then return the second number as the sum
    elif a == c:
        return b
    # if second & third numbers are same, then return the first number as the sum
    elif b == c:
        return a
    # return the sum of given numbers if all 3 are different from each other
    else:
        return a+b+c

# test the lone_sum() function with various arguments
print("lone_sum of 10, 10, 10 should be 0: " + str(lone_sum(10, 10, 10)))
print("lone_sum of 1, 2, 3 should be 6: " + str(lone_sum(1, 2, 3)))
print("lone_sum of 1, 2, 1 should be 2: " + str(lone_sum(1, 2, 1)))
print("lone_sum of 4, 5, 6 should be 15: " + str(lone_sum(4, 5, 6)))