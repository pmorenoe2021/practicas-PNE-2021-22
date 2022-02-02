# --- EXCERCISE 1:
N = 11
# we create a constant with  uppercase leters and equal it to a number

n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
for i in range(2, N): #we start from 2 because we already printed the first 2 numb, if we start from 0 we will print 13 numb
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num
print()# if you want to run it in the terminal to be more separated