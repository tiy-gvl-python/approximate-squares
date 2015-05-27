import math
import cmath


# functions

# returns the next estimate using Newton's Method
def new_estimate(old_estimate,number_):
    return old_estimate - (old_estimate**2 - number_)/(2*old_estimate)

# returns the number truncated to the requested number of decimals
def truncate(number_,decimals=0):
    return math.floor(abs(number_)*(10**decimals))/(10**decimals)

# returns true if estimates are equal to the specified decimal place
def compare_estimates(estimate1,estimate2,decimals):
    return truncate(estimate1,decimals) == truncate(estimate2,decimals)

# prints the provided loop number and estimate
def print_details(estimate,loop):
    print("{}: {}".format(loop,estimate))

# Prompt for number
input_number = input("Enter a number > ")

# Convert input_number to a float
try:
    number = float(input_number)
except ValueError:
    print ("You did not enter a number.")
    exit()

# Original Estimate
current_estimate = number / 2
if number < 0:
    current_estimate += 1j * number / 2

number_of_loops = 1
print_details(current_estimate,0)

# Algorithm
while True:
    # Calculate new estimate
    next_estimate = new_estimate(current_estimate,number)
    # Print current information
    print_details(next_estimate,number_of_loops)
    # Compare new estimate to old estimate
    if compare_estimates(next_estimate,current_estimate,2):
        # If hundredth's place hasn't changed, break
        break
    # Else repace old estimate with new estimate and repeat
    current_estimate = next_estimate
    number_of_loops += 1

# Print Results
print("The square root of {} is {}.".format(number,current_estimate))
