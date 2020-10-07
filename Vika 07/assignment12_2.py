def iseven(n_int):
    if n_int % 2 == 0:
        return True
    return False

def remove_evens(int_list):
    [int_list.remove(elem) for elem in int_list[:] if iseven(elem)]

def remove_evens2(int_list):
    new_list = []
    [new_list.append(ele) for ele in int_list if not(iseven(ele)) ]
    return new_list


# Main starts here
a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)