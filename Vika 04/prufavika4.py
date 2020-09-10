my_int = int(input('Give me an int >= 0: '))
quot_int = my_int
bin_str = ''

while quot_int > 0:

    bin_str += str(quot_int % 2)
    quot_int = quot_int // 2
    print(quot_int)
    print(bin_str)

bin_str = bin_str[::-1]


print("The binary of {} is {}".format(my_int,bin_str))