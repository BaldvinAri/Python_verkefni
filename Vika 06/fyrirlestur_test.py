





def read_file(file_object, line_num):
    counter = 1
    for line in file_object:
        line = line.strip()
        if line_num == counter:
            print(line)
            break

def get_line_number():
    try:
        line_num = int(input("Enter a line number: "))
        return line_num
    except ValueError:
        return 0

def main():
    line_num = get_line_number()
    print(line_num)

main()