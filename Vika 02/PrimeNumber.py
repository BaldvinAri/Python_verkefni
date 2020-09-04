n = int(input("Input a natural number: ")) # Do not change this line
counter = 2
# Fill in the missing code below

if n == 2:
    prime = True
elif n < 2:
    prime = False
elif n % 2 == 0:
    prime = False
else:
    while counter < n:
        rem = n % counter
        if rem == 0:
            prime = False
            break
        counter += 1
    else:
        prime = True

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")