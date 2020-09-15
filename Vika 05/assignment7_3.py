# max_of_three function definition goes here
def max_of_three(fir,sec,thi):
    if fir > sec and fir > thi:
        return fir
    elif sec > fir and sec > thi:
        return sec
    else:
        return thi

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

maximum = max_of_three(first,second,third)

# Call the function here
print("Maximum:", maximum)