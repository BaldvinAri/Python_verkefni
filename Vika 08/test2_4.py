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

def nested_list_index( nested_list , index_from , index_to ):
    """
    Indexes a part of lists in a list and returns a new list with those values.
    """
    new_list = []
    return [ lst[index_from : index_to] for lst in nested_list]

def get_total_freq( nested_list , index ):
    """
    Takes in a nested list and an index number. 
    Returns the sum of all elements in the lists index.
    """
    return sum( lst[index] for lst in nested_list )

def fiftyth_pre_mark( genderlist, gender_total_freq, index ):
    """
    Takes in a gender nested list, total frequency of the gender and an index integer.
    Returns the 50th percentile rank mark for that gender.
    """
    MARK_NUM = 0
    mark_fifty = gender_total_freq / 2
    freq_sum = 0

    for lst in genderlist:
        mark = lst[ MARK_NUM ]
        freq_sum += lst[ index ]

        if mark_fifty < freq_sum:
            return mark

def print_data(org_list, boys, girls, boys_freq, girls_freq, mark_boys, mark_girls):
    """
    Takes in results and prints
    """
    print( org_list[:2] ) # First 2 boys and girls
    print( boys[:5] ) # First 5 boys
    print( girls[:5] ) # First 5 Girls
    print("Total frequency of boy names: {}".format( boys_freq )) 
    print("Total frequency of girl names: {}".format( girls_freq ))
    print("50th percentile rank for boys: {}".format( mark_boys ))
    print("50th percentile rank for girls: {}".format( mark_girls ))



def main():
    fileobject, filename = try_open_file() 
    if fileobject:

        fixed_list = list_2_int_list( read_file_lines(fileobject) ) # 1 -- Convert file obj to int and str list
        
        boys_list = nested_list_index(fixed_list, 1, 3) # 2 -- Boy names and frequencies
        girls_list = nested_list_index(fixed_list, 3, 5) # 2 -- Girl names and frequencies

        boys_freq = get_total_freq(boys_list, 1) # 2 -- Boys total frequencies
        girls_freq = get_total_freq(girls_list, 1) # 2 -- Girls total frequencies

        mark_boys = fiftyth_pre_mark(fixed_list, boys_freq ,2) # 3 -- Boys 50th percentile rank
        mark_girls = fiftyth_pre_mark(fixed_list, girls_freq ,4) # 3 -- Girls 50th percentile rank

        print_data(fixed_list, boys_list, girls_list, boys_freq, girls_freq, mark_boys, mark_girls )
            # Print results

    else:
        print( "File {} not found".format(filename) )

main()