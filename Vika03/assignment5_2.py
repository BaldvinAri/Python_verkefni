n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1_int = 1
n2_int = 2
n3_int = 3
flipflop = 1

for i in range(1,n+1):

    if i < 4:
        print(i)
    else:
        

        if flipflop == 1:
            n1_int = n1_int + n2_int + n3_int
            print(n1_int)
            flipflop = 2
        
        elif flipflop == 2:
            n2_int = n1_int + n2_int + n3_int
            print(n2_int)
            flipflop = 3
        
        elif flipflop == 3:
            n3_int = n1_int + n2_int + n3_int
            print(n3_int)
            flipflop = 1







# Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …