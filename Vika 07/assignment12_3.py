import string

def get_file_as_str():
    file_name = input("Enter filename: ")
    file_obj = open(file_name,"r")
    file_str = file_obj.read()
    return file_str

def remove_letter_from_string(lett,i_str):
    new_str = ""
    for i in i_str:
        if lett != i:
            new_str += i
    return new_str

def remove_punct(stri):
    punctuations = string.punctuation
    punctuations = remove_letter_from_string("-",punctuations)
    new_str = ""
    for letter in stri:
        if letter not in punctuations:
            new_str += letter
    return new_str

def remove_multiples(n_list):
    for i in n_list[:]:
        while n_list.count(i) > 1:
            n_list.remove(i)


file_str = get_file_as_str()
nice_str = remove_punct(file_str).strip()
nice_list = nice_str.split()
remove_multiples(nice_list)
print( sorted(nice_list) )








