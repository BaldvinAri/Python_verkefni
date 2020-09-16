def palindrome(string):
    new_string = ''
    for n in string:
        if n.isalpha():
            new_string += n

    backwardsstring = new_string[::-1]
    return new_string.lower() == backwardsstring.lower()
        
        
in_str = input("Enter a string: ")

if palindrome(in_str):
    print("\"{}\" is a palindrome.".format(in_str))
else:
    print("\"{}\" is not a palindrome.".format(in_str))

