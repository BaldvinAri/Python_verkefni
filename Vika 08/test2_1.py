def get_options():
    """
    Print choices and return input option
    """
    print("1: Compute the sum of 1..n")
    print("2: Compute the product of 1..n")
    print("9: Quit") 

    return input("Choice: ")
    

def get_number():
    """
    Checks if input is a valid integer. 
    Returns the integer if true, else return None
    """
    n = input("Enter value for n: ")
    try:
        return int(n)
    except ValueError:
        return 

def sum_of_nth( n ):
    """
    Takes in an integer >= 0 and returns the sum of 
    1 to n-th integer.
    """
    if n > 0:
        return sum( range(n + 1) )
    else:
        return 0

def prod_of_nth(n):
    """
    Takes in an integer >= 0 and returns the 
    factorial value of that integer.
    """
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial





COMPUTE_SUM = "1"
COMPUTE_PRODUCT = "2"
# ... add options here
EXIT = "9"

choice = ""

while choice != EXIT: 
    choice = get_options() 

    if choice == COMPUTE_SUM:
        nth_num = get_number()

        if nth_num or nth_num == 0: # If integer >= 0
            sum_ = sum_of_nth( nth_num )
            print("The result is: {}".format( sum_ ))

    elif choice == COMPUTE_PRODUCT:
        nth_num = get_number()

        if nth_num or nth_num == 0: # If integer >= 0
            prod_ = prod_of_nth( nth_num )
            print("The result is: {}".format( prod_ ))
