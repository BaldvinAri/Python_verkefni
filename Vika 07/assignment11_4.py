# user input 
# change numbers seperated by space into list of floats
# length of list must be at least 3

numbers_lst = input("Enter scores separated by space: ").split()

if len( numbers_lst ) < 2:
    print("At least two scores needed!")
else:
    float_list = [float(num) for num in numbers_lst]

    float_list.remove(min(float_list))
    float_list.remove(min(float_list))

    print("Sum of scores (two lowest removed):",sum( float_list ))