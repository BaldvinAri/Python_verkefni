def get_info():
    name = input("Name: ")
    number = input("Number: ")
    return name, number

def process_dict( dict_ ):
    N_list = []
    for item in dict_.items():
        N_list.append(item)
    return sorted(N_list)

def main():
    YES = "y"
    NO = "n"
    choice = YES
    phone_dict = {}

    while choice == YES:
        name, number = get_info()
        phone_dict[name] = number

        choice = input("More data (y/n)? ")

    phone_book = process_dict( phone_dict )

    print(phone_book)


main()

