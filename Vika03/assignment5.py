num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while -1 < num_int:

    if num_int >= max_int:
        max_int = num_int

        # Do not change this line
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)

# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.