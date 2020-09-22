temp_file = open("text.txt","r") # open the file for reading
for line_str in temp_file: # iterate through the file via the file object
    print(line_str,end='')