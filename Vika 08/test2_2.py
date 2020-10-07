def try_open_file():
    """
    Try to open filename from input. Returns file object if file exists,
     returns None if it does not.
    """
    filename = input("Enter file name: ")
    try:
        return open(filename,"r") , filename
    except FileNotFoundError:
        return None, filename

def read_file_lines(file_obj):
    """
    Takes in an open text file, splits words into a list, and splits lines into a nested list.
    returns a nested list.
    """
    new_list = []
    for line in file_obj:
        new_list.append( line.split() )
    return new_list

def list_2_int_list(list_of_lists):
    """
    Takes in a nested list and converts strings to integers if possible.
    returns a new nested list with all elements integers or parts of it integers.
    """
    new_list = []
    for lst in list_of_lists:
        new_list.append( try_make_int(lst) )
    return new_list

def try_make_int(lst):
    """
    Takes in a list of different types, converts to integers if possible.
    Returns a new list with all elements integers or parts of it integers.
    """
    new_list = []
    for elem in lst:
        try:
            new_list.append( int(elem) )
        except ValueError:
            new_list.append( elem )
    return new_list
    

def print_data(org_list):
    """
    Takes in results and prints
    """
    print( org_list[:2] ) # First 2 boys and girls



def main():
    fileobject, filename = try_open_file() 
    if fileobject:

        fixed_list = list_2_int_list( read_file_lines(fileobject) ) # 1 -- Convert file obj to int and str list

        print_data(fixed_list)
            # Print results

    else:
        print( "File {} not found".format(filename) )

main()