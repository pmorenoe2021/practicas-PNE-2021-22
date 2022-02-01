# Function for calculating the sum of the
# N first integer numbers


def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


# -- The main program starts here
print("Sum of the 20 first integers: ", sumn(20))
print("Sum of the 100, frist integers: ", sumn(100))

#with step into, you will see everythin step by step, entering each of the functions.
# i can step out and we will see a change in the final result.