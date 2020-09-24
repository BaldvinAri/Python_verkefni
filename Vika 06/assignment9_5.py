def open_file(filename):
    return open(filename , "r")

def nonewline(file_object):
    return file_object.strip().replace(" ","\n")

# Main program starts here
filename = input("Enter filename: ")

for line in open_file(filename):
    print( nonewline(line) )
