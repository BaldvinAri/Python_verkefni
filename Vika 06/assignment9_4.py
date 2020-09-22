# Your functio
def open_file(filename):
    try:
        file_object = open(filename , "r")
        return file_object
    except FileNotFoundError:
        return

def find_longest(file_obj):
    return nospaces_file_object( max( file_obj , key = len ) )

def nospaces_file_object(file_object):
    return file_object.replace("\n","")


# Main program starts here
filename = input("Enter filename: ")
file_object = open_file(filename)
if file_object:
  longest_word = find_longest(file_object)
  print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
  file_object.close()
else:
  print("File not found")