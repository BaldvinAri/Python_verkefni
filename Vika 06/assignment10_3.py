# Your functions should appear here
def add_to_list(n_list):
    new_list = [user_input()]
    return n_list + new_list

def first_last_same(final_list):
    new_list = []
    for i in final_list:
        if i[-1] == i[0] and len(i) > 1:
            new_list += [i]
    return new_list


def user_input():
    return input("Enter word to be added to list: ")


# Main program starts here
# It should mostly be a sequence of function calls


EXIT = "x"
words = list( [user_input()] )

while words[-1] != EXIT:
    words = add_to_list(words)

words.pop()
print(words)
for n in first_last_same(words):
    print(n)
