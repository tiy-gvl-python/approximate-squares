import math
square_root=int(input("Enter a positive number:"))
#guess=int(input("What is your initial guess? "))
guess=1
count=0
for x in range(1000):
    quotient=square_root/guess
    #print(quotient)
    ratio=(guess+quotient)/2
    #print(ratio)
    guess=ratio
    #print(count)
    #print(guess)
try:
    assert ratio==math.sqrt(square_root)
    print(ratio)
except:
    print("its not right")
    percentage=ratio/math.sqrt(square_root)*100
    print("error percentage {}".format(percentage))
    
