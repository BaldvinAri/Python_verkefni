percent_float = float(input("What is your percentage? "))

if 85 <= percent_float < 100:
    print("you received an A")
elif 70 <= percent_float < 85:
    print("you received a B")
elif 55 <= percent_float < 70:
    print("you received a C")
else:
    print("oops, not good")
