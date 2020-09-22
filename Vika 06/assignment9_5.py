def open_file(filename):
    file_object = open(filename , "r")
    return file_object


def nonewline(file_object):
    return file_object.replace("\n"," ")


# Main program starts here
filename = input("Enter filename: ")

for line in open_file(filename):
    print(nonewline(line))
