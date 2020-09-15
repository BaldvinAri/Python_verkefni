def is_prime(n):
    counter = 2
    if n == 2:
        return True
    elif n < 2:
        return False
    elif n % 2 == 0:
        return False
    else:
        while counter < n:
            rem = n % counter
            if rem == 0:
                return False
            counter += 1
        else:
            return True

    
max_num = int(input("Input an integer greater than 1: "))
for i in range(2,max_num + 1):
    if is_prime(i):
        print(i,"is a prime")
    else:
        print(i,"is not a prime")