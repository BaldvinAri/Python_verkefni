def open_file(filename):
    return open(filename , "r")

def strlist_2_intlist(n_list):
    for i in range( len(n_list) ):
        n_list[i] = int(n_list[i]) 
    return n_list

def read_lines(file_obj,N):
    new_list = []
    for line in file_obj:

        if len( line.split() ) == N:
            
            new_list.append( strlist_2_intlist( line.split() ) )
            

    return new_list

def vector_sum(vectors,N):
    sum_of = 0
    n_list = []
    vector_sum = []
    for i in range(N):
        summ = 0
        for n in range(N):
            summ += vectors[n][i]
        vector_sum.append(summ) 
    return vector_sum




N_INT = 3


filename = input("Enter filename: ")
filen = open_file(filename)
read = read_lines(filen,N_INT)
a = vector_sum(read,N_INT)
print(read)
print(a)