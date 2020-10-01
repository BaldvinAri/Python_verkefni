


a  = [1.4, 6.32, 5.1, 7.4, 1.4, 6.32, 5.1, 7.4]
print("Original list of floats: ",a)

b = [str(i) for i in a]
print("Original list of floats converted to string",b)

Thelist = ", "

c = Thelist.join(b)
print("A string of every element in list with a seperator", c)