#Calculates square roots with Newton's Method.
n = int(input("Enter the number to solve "))
g = int(input("Enter the guess "))
true = "negative"
false = "positive"
sum = 0

def num_check(n, g):
    if n < 0:
        print("invalid number type for n")
        return true
    elif g < 0:
        print("invalid number type for g")
        return true
    else:
        return false

def average(n, g):
    return ((n/g) + g)/2

for i in range(10):
    if num_check(n, g) == "negative":
        break
    g = average(n, g)
    sum = sum + i
    print("Newtons square root is {}".format(g))
