integer = int(input("What is your number? "))
guess = int(input("What is your guess? "))
for i in range(10):
    guess = ((integer/guess) + guess) / 2

print(guess)
