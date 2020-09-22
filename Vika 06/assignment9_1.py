def file_read(file_name):
    #file_text = ""
    file_object = open( file_name , "r" )
    return file_object.read()
    #for line in file_object:
    #    file_text += line
    #return file_text

def nospaces_file_object(file_object):
    return file_object.strip().replace(" ","").replace("\n","")

# Main starts here

file_name = input("Enter filename: ")
text = file_read(file_name) 
result = nospaces_file_object(text)

print(result)