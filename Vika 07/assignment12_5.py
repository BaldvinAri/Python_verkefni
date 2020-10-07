def get_numbers():
    numbers = input("Enter integers separated with commas: ")
    return numbers.split(",")

def isdigit_list(n_list):
    for i in n_list:
        if not i.isdigit():
            return False
    return True

def str_list_2_int(n_list):
    return [int(elem) for elem in n_list]

def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def num_list_2_prime(n_list):
    newlist = []
    for i in n_list:
        if is_prime(i):
            newlist.append(i)
    return newlist

def remove_multiples(n_list):
    for i in n_list[:]:
        while n_list.count(i) > 1:
            n_list.remove(i)

num_list = get_numbers()

if isdigit_list(num_list):
    new_list = str_list_2_int(num_list)
    new_list_sorted = sorted( new_list )
    prime_list = num_list_2_prime( new_list_sorted )
    remove_multiples(prime_list)
    

    min_num = min(new_list)
    max_num = max(new_list)
    avg_num = sum(new_list) / len(new_list)

    print("Input list:",new_list)
    print("Sorted list: ",new_list_sorted)
    print("Prime list: ",prime_list)
    print("Min: {}, Max: {}, Average: {:.2f}".format(min_num,max_num,avg_num))

else:
    print("Incorrect input!")        
# The main program starts here
