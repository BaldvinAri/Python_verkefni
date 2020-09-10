# Author: Baldvin Ari Eiríksson #

newpass_str = 0
invalid_int = 0
valid_int = 0
attempts_int = 0

while True:

    lower_bool = False
    upper_bool = False
    num_bool = False

    newpass_str = input("Enter a new password: ")

    if newpass_str == 'q':
        break
        # Exit loop
    
    attempts_int += 1
        # No. attempts tried
    
    pass_len_int = len(newpass_str)

    if not(6 <= pass_len_int <= 20):
        print('Invalid length')
        invalid_int += 1
        continue
            # Condition 1
            # Repeat loop if invalid

    for n in range( pass_len_int ):

        if newpass_str[n].islower():
            lower_bool = True
                # Condition 2

        elif newpass_str[n].isupper():
            upper_bool = True
                # Condition 3

        elif newpass_str[n].isnumeric():
            num_bool = True
                # Condition 4
 
    if lower_bool and upper_bool and num_bool:
        print('Valid password of length',pass_len_int)
        valid_int += 1
        continue
            # Repeat loop if valid
            # Finish the loop if invalid

    invalid_int += 1

    if not(lower_bool):
        print('At least one lower case letter needed')

    if not(upper_bool):
        print('At least one upper case letter needed')

    if not(num_bool):
        print('At least one number needed')

# Loop finished
print('You tried {} passwords, {} valid, {} invalid'.format(attempts_int, valid_int, invalid_int))

