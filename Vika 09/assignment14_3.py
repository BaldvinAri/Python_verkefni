import string
from operator import itemgetter

def try_open_file(filename):
    try:
        return open(filename,"r")

    except FileNotFoundError:
        print( "File {} not found!".format(filename) )
        return

def remove_letter_from_string(lett, i_str):
    new_str = ""
    for i in i_str:
        if lett != i:
            new_str += i
    return new_str

def remove_punct(stri):
    punctuations = string.punctuation
    #punctuations = remove_letter_from_string("'",punctuations)
    #punctuations = remove_letter_from_string("-",punctuations)
    new_str = ""
    for letter in stri:
        if letter not in punctuations:
            new_str += letter
    return new_str

def biogram_tuples(L):

    plus_tup = L.copy()
    plus_tup.pop(0)
    plus_tup = tuple( plus_tup )
    tup = tuple(L)

    return list( zip(tup,plus_tup) )

def word_list_to_counts(tlist):
    cnt_d = {}
    for key in tlist:
        if key not in cnt_d:
            cnt_d[key] = 1
        else:
            cnt_d[key] += 1
    return cnt_d




def main():
    file_ = input("Enter name of file: ")
    fobj = try_open_file( file_ )
    ftext = fobj.read().lower()
    ftext = ftext.split()
    ftext = [word.strip(string.punctuation) for word in ftext]
    flist = biogram_tuples( ftext )
    f_dict = word_list_to_counts( flist )

    L_sorted = sorted(f_dict.items(),key = itemgetter(0))
    L_sorted = sorted(L_sorted,key = itemgetter(1),reverse = True)

    if len( L_sorted ) > 10:
        print(L_sorted[:10])
    else:
        print( L_sorted )
    
    
main()