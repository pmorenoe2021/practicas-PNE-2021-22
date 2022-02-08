#EXCERCISE 2: Convert the previous program into the function fibon(n) that calculates the nth Fibonacci term and return it
# The main program should call the fibon() function and print the 5th, 10th and 15th terms in the console
def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(2, n):
            num = n1 + n2
            n1 = n2
            n2 = num
        return num
print("5th FIBONACCIS TERM",fib(5))
print("11th FIBONACCIS TERM",fib(11))
print("55h FIBONACCIS TERM",fib(55))
#NEVER WRITE THE REUTURN INSIDE A LOOP

