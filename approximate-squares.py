
integer = int(input("What is your number? "))
guess = int(input("What is your guess? "))
count = 0

for i in range(10):
    guess = ((integer/guess) + guess) / 2
    count += 1
    print(guess)
