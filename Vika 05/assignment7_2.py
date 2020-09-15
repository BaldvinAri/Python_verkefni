def count_digits(string):
    counter = 0
    for i in string:
        if i.isdigit():
            counter += 1

    return counter

input_str = input("Enter a string: ")
digit_count = count_digits(input_str)
# Call the function here

print("No. of digits:", digit_count)