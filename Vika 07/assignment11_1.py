#list_to_int_tuple function goes here
def list_to_int_tuple(n_list):
    new_list = []
    for elem in n_list:
        if isvalid_int(elem):
            new_list.append( int(elem) )
    return tuple(new_list)

def isvalid_int(n ):
    try:
        return int(n)
    except ValueError:
        return


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_int_tuple(a_list)
print(a_tuple)