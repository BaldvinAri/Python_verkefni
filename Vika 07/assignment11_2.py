def iseven(n_int):
    if n_int % 2 == 0:
        return True
    return False

def even_sum(n_list):
    even_list = [elem for elem in n_list if iseven(elem)]
    return sum(even_list)

def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    a_list = [int(i) for i in a_list]
    return a_list

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
