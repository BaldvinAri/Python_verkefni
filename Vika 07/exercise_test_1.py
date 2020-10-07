def check_length(L):
    if len(L) < 2:
        return False
    return True

def list_2_floatlist(L):
    return [float(s) for s in L]

def remove_min_from_list(L,n_times):
    for i in range(n_times):
        L.remove(min(L))


def main():

    numbers = input("Enter scores separated by space: ").split()

    if check_length(numbers):
        numbers_floatlist = list_2_floatlist( numbers )
        remove_min_from_list(numbers_floatlist, 2)

        print("Sum of scores (two lowest removed): {}".format(sum( numbers_floatlist )))


    else:
        print("At least two scores needed!")




main()