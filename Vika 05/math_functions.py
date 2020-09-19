#  Import packages  #

import math as m

#  Define Functions  #

def text_print():
    a = "Please choose one of the options below:"
    b = "a. Display the sum of the first N natural numbers."
    c = "b. Display the sum of the first N Fibonacci numbers."
    d = "c. Display the approximate value of e using N terms."
    e = "x. Exit from the program."
    print( "{}\n{}\n{}\n{}\n{}\n".format(a,b,c,d,e) )


def isstr_geq_2(n_str):
    """ Returns True if the string is a digit
     and is greather than or equal to 2 (geq) """
    N_MIN = 2
    if n_str.isdigit():
        if int(n_str) >= N_MIN:
            return True
    return False

def int_2_str(num_str):
    """ Converts string to integer """
    return int(num_str)


def sum_natural(n_str):
    """ Returns the sum of N many
    natural numbers.
    Returns None if input is not a valid number """
    if isstr_geq_2(n_str):
        n_int = int_2_str( n_str )
        return sum( range( 1 , n_int + 1) )
    return 

def fibonacci_sum(n_str):
    """ Returns the sum of N many 
    elements of the fibonacci series.
    Returns None if input is not a valid number  """
    if isstr_geq_2(n_str):
        n_int = int_2_str( n_str )
        num_1 = 0
        num_2 = 1
        num_3 = 0
        num_sum = 1
        for i in range( n_int - 2 ):
            num_3 = num_1 + num_2
            num_1 = num_2
            num_2 = num_3
            num_sum += num_3
        return num_sum
    return

def approximate_euler(n_str):
    """ Returns the elements of N many elements
    of the approximate euler number.
    Returns None if input is not a valid number """
    if isstr_geq_2(n_str):
        n_int = int_2_str( n_str )
        exp_approx = 0
        
        for k in range( 0 , n_int ):
            exp_approx += 1 / m.factorial(k)
        return round( exp_approx , 5 )
    return


#   Variables and fixed numbers and strings  #

x_STR = "x"
a_STR = "a"
b_STR = "b"
c_STR = "c"

option = ""


#   Main program    #

while True:

    if option not in [a_STR , b_STR , c_STR]:
        text_print()
        # only prints if incorrect option is 
        # chosen and in the beginning

    option = input("Enter option: ")

    if option == x_STR:
        break
        # Exit program

    if option not in [a_STR , b_STR , c_STR]:
        print("Unrecognized option",option)
        continue
        # Repeat print command if incorrect 
        # option is chosen

    n_str = input("Enter N: ")

    if option == a_STR:
        output = sum_natural(n_str)
        output_text = "Natural number sum:"

    elif option == b_STR:
        output = fibonacci_sum(n_str)
        output_text = "Fibonacci sum:"

    elif option == c_STR:
        output = approximate_euler(n_str)
        output_text = "Euler approximation:"
     
    if output != None:
        print( output_text , output ,"\n")
    else:
        print( "Error:", n_str, "was not a valid number.\n" )
        # If functions return None, an error message is printed
        

 