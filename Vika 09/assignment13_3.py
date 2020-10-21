def menu_selection():
    print("Menu: ")
    return input("(a)dd, (r)emove, (f)ind: ")

def execute_selection(opt,D):
    if opt == "a":
        key = input("Key: ")
        val = input("Value: ")
        add_to_dict(D,key,val)
        
    elif opt == "r":
        key = input("Key to remove: ")
        remove_from_dict(D,key)

    elif opt == "f":
        key = input("Key to locate: ")
        val = find_key(D,key)

        if val:
            print("Value: {}".format(val))
        else:
            print("Key not found.")

def add_to_dict(D,key,val):
    if key not in D:
        D[key] = val
    else:
        print("Error. Key already exists.")

def remove_from_dict(D,key):
    try:
        D.pop(key)
    except KeyError:
        print("Key not found.") 

def find_key(D,key):
    val = D.get(key)
    if val:
        return val
    else:
        return

def dict_to_tuples( dict_ ):
    N_list = []
    for item in dict_.items():
        N_list.append(item)
    return N_list



def main():
    more_input = True
    a_dict = {}
    
    while more_input:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more_input = again.lower() == 'y'
    
    tuple_list = dict_to_tuples(a_dict)
    print(sorted(tuple_list))

main()