def print_options():
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")
    return input("Set operation: ")
    
    return line1

def str_2_int_list(L):
    return [ int(s) for s in L ]

def num_set_comma(num):
    return set( str_2_int_list( num.strip().split(",") ) )


def main():
    
    ints_1 = input("Input a list of integers separated with a comma: ")
    ints_2 = input("Input a list of integers separated with a comma: ")
    set_1 = num_set_comma( ints_1 )
    set_2 = num_set_comma( ints_2 )
    print(set_1)
    print(set_2)
    choice = ""
    
    while choice != "4":
        choice = print_options()
        if choice == "1":
            print(set_1 & set_2)

        elif choice == "2":
            print(set_1 | set_2)

        elif choice == "3":
            print(set_1 - set_2)


main()


