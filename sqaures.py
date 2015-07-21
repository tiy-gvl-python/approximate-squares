# approximate sqaure formuli go below
number = float(input("Pick a number: "))
guess = float(input('Guess the numbers sqaure root: '))



def aproximate_sqaure(x, y):
    actual_sqrt = x ** .5
    guess = y

    while guess != actual_sqrt:
        guess = (guess + (x / guess)) / 2
        print(guess)

    return print("newtonian sqrt: {}\nactual_sqrt: {}".format(guess, actual_sqrt))

aproximate_sqaure(number, guess)
