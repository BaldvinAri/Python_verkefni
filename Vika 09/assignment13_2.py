import string

def get_word_list(f_obj):
    file_text = f_obj.read().lower()
    return remove_punct( file_text ).strip().split()


def word_list_to_counts(w_lst):
    new_d = {}
    for word in w_lst:
        if word not in new_d:
            no_words = w_lst.count(word)
            new_d[word] = no_words
    return new_d

def dict_to_tuples( dict_ ):
    N_list = []
    for item in dict_.items():
        N_list.append(item)
    return N_list


def remove_letter_from_string(lett, i_str):
    new_str = ""
    for i in i_str:
        if lett != i:
            new_str += i
    return new_str

def remove_punct(stri):
    punctuations = string.punctuation
    punctuations = remove_letter_from_string("'",punctuations)
    punctuations = remove_letter_from_string("-",punctuations)
    new_str = ""
    for letter in stri:
        if letter not in punctuations:
            new_str += letter
    return new_str





def main():
    filename = input("Name of file: ")
    file_object = open(filename)
    word_list = get_word_list(file_object) 
    file_object.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuples(word_count_dict)
    print(sorted(word_count_tuples))
    
main()