# Ask the user to enter how many numbers they will input
N = int(input("How many numbers will you enter? "))

# Prepare a place to keep the numbers
numbers = []

# Get each number from the user, one at a time
for i in range(N):
    num = int(input(f"Enter number {i+1} of {N}: "))
    numbers.append(num)  # Add the number to our list

# Now ask for one more number to search for in our list
X = int(input("Which number are you looking for? "))

# Look for that number in the list
if X in numbers:
    # If found, tell the user where it is (note: we start counting from 1)
    print(f"Found it! It's at position {numbers.index(X) + 1}.")
else:
    # If not found, let the user know
    print("Sorry, that number isn't in the list.")
