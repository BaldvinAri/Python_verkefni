import string

# Implement a function here
def un_lett(n_str):
    n_list = list(n_str)
    letters_list = list(string.ascii_letters)
    new_list = []
    for i in n_list:
        if i in letters_list:
            new_list.append(i)
            letters_list.remove(i)
    return new_list


# Main starts here
sentence = input("Input a sentence: ")
# Call the function here




print("Unique letters:", un_lett(sentence))

