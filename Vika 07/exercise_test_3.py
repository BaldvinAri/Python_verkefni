def get_list():
    return input("Enter elements of a list separated by space: ").split()

def remove_duplicates(L):
    new_list = []
    for num in L:
        if not num in new_list:
            new_list.append(num)
    return new_list

def intersection(L1,L2):
    return [num for num in L1 if num in L2]

def union(L1,L2):
    new_list = L1 + L2
    sorted_new_list = sorted(new_list)
    return remove_duplicates( sorted_new_list )

def list_2_intlist(L):
    return [int(s) for s in L]

def main():

    list_a = remove_duplicates( get_list() )
    list_b = remove_duplicates( get_list() )
    int_list_a = list_2_intlist(list_a)
    int_list_b = list_2_intlist(list_b)

    sorted_a_list = sorted(int_list_a)
    sorted_b_list = sorted(int_list_b)

    print( "Set 1: {}".format(sorted_a_list) )
    print( "Set 2: {}".format(sorted_b_list) )

    inter_list = intersection(sorted_a_list,sorted_b_list)
    print( "Intersection: {}".format(inter_list) )

    union_list = union(sorted_a_list,sorted_b_list)
    print( "Union: {}".format(union_list) )

    

main()