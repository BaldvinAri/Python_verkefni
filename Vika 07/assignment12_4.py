def get_numbers():
    numbers = input("Enter elements of list separated by commas: ")
    return numbers.split(",")

def isdigit_list(n_list):
    for i in n_list:
        if not i.isdigit():
            return False
    return True

    
num_list = get_numbers()
if isdigit_list(num_list):
    
    check_count = input("Consecutive check: ")
    if num_list.count(check_count) > 1:
        print(True)
    else:
        print(False)
else: 
    print("Error: enter only integers.")

    
