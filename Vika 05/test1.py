def valid_date(mella):
    if len(mella) == 8:
        if mella[2] == '.' and mella[5] == '.':
            if "01" <= mella[:2] <= "31":
                if "01" <= mella[3:5] <= "12":
                    if "00" <= mella[6:] <= "99":
                        return True
    return False


date_str = input("Enter a date: ")

if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")
