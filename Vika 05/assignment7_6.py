def valid_date(date):
    if len(date) == 8:
        if date[2] == "." and date[5] == ".":
            if "01" <= (date[0] + date[1]) <= "31":
                if "01" <= (date[3] + date[4]) <= "12":
                    if "00" <= (date[6] + date[7]) <= "99":
                        return True
    return False


date_str = input("Enter a date: ")

if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")  