def divide_safe(num1_str, num2_str):
    try:
        num1_float = float(num1_str)
        num2_float = float(num2_str)

        return round( num1_float / num2_float , 5 )

    except ValueError:
        return
    except ZeroDivisionError:
        return


num1_str = input('Input first number: ')
num2_str = input('Input second number: ')

result = divide_safe(num1_str, num2_str)

print(result)