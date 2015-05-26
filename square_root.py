import math
import cmath
square_root=int(input("Enter a positive number:"))
#guess=int(input("What is your initial guess? "))
guess=1
imagineguess=1j
count=0
for x in range(1000):
    if 0+square_root<0:
            quotient=square_root/imagineguess
            #print(quotient)
            ratioi=(imagineguess+quotient)/2
            #print(ratio)
            imagineguess=ratioi
            #print(count)
            #print(guess)
            string_ratioi=str(ratioi)
            #print(string_ratioi)
    if 0+square_root>=0:
        quotient=square_root/guess
        #print(quotient)
        ratio=(guess+quotient)/2
        #print(ratio)
        guess=ratio
        #print(count)
        #print(guess)
        """string_ratio=str(ratio)
        decimal_local=string_ratio.find('.')
        print(decimal_local)
        digits_100s=[]
        try:
            digits_100s=[string_ratio[decimal_local+1],string_ratio[decimal_local+2]]
        except:
            print("Ey YO THIS is a print mes")"""
if 0+square_root>=0:
    try:
        assert ratio==math.sqrt(square_root)
        print(ratio)
    except:
        print("its not right")
        percentage=ratio/math.sqrt(square_root)*100
        print("error percentage {}".format(percentage))
else:
    print(string_ratioi)
