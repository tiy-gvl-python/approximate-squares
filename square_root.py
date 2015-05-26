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
    string_ratio=str(ratio)
    decimal_local=string_ratio.find('.')
    print(decimal_local)
    try:
        print(string_ratio[decimal_local+1])
        print(string_ratio[decimal_local+2])
    except:
        print("Ey YO THIS is a print mes")

try:
    assert ratio==math.sqrt(square_root)
    print(ratio)
except:
    print("its not right")
    percentage=ratio/math.sqrt(square_root)*100
    print("error percentage {}".format(percentage))
