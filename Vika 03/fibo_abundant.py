""" Author: Baldvin Ari Eiríksson """

ch = str( input("Input f|a|b (fibonacci, abundant or both): ") )

    # Fibonacci Sequence
if ch == "f" or ch == "b":

    seq_len = int( input("Input the length of the sequence: ") )
    print("Fibonacci Sequence:")
    print("-------------------")

    for i in range(0, seq_len - 1):
        if i == 0:
            summ1 = 0
            summ2 = 1
            flipflop = True 
            print(summ1)

        if i == 1:
            print(summ2)

        else:   # Flipflop function to 
                # overwrite the lesser number

            if flipflop == True:
                summ1 += summ2
                print(summ1)
                flipflop = False
                     
            elif flipflop == False:
                summ2 += summ1
                print(summ2)
                flipflop = True


    # Abundant numbers
if ch == "a" or ch == "b":

    max_num = int( input("Input the max number to check: ") )
    print("Abundant numbers:")
    print("-----------------")

    for i in range(1, max_num + 1): 
        adder = 0
            # Reset adder for next the number.

        for n in range(1, i):
    
            if i % n == 0:
                adder += n
                    # If number has 0 reminder,
                    # sum it up.

        if adder > i:
            print(i)
                # If sum of proper divisors is bigger.

