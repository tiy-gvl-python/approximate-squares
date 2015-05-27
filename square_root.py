#Hard Mode
p  = int(input("What positive number do you want to find the Square Root? > "))
g = int(input("Guess what you think the Square Root may be. > "))
count = 0

while count <= 8:
    x = p / g
    g = (x + g) / 2
    count += 1
    print("Current guess is {} on iteration number {}".format(g, count + 1))
print("The Square Root of {} is {}.".format(p, g))
