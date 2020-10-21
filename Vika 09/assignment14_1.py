def remove_duplicates(L):
    new_list = []
    for num in L:
        if not num in new_list:
            new_list.append(num)
    return new_list

def same_letters(words):
    a_list = [s for s in words[1] if s in words[0]]
    return sorted(remove_duplicates( a_list ))

def set_letters(words):
    word1 = set(words[0])
    word2 = set(words[1])
    return sorted( list(word1 & word2) )

def main():
    name = input("Enter name: ").lower().strip().split()
    list_same = same_letters( name )
    set_same = set_letters( name )
    print("{}\n{}".format( list_same, set_same ))

main()

