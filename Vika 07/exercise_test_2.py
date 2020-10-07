def try_open_file(filename):
    try:
        fileob_ = open(filename,"r")
        return fileob_.read()

    except FileNotFoundError:
        print( "File {} not found!".format(filename) )
        return

def count_extra_words(file_str):
    sep_word = ",.!?"
    extra_words = 0
    for s in file_str:
        if s in sep_word:
            extra_words += 1

    return extra_words

def main():
    file_name = input("Enter filename: ")
    file_ = try_open_file(file_name)
    if file_:
        words = file_.strip().split()

        counter = len( words ) + count_extra_words( file_ )

        print(counter)

main()