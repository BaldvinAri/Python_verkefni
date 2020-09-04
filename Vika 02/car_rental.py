"""     Author: Baldvin Ari Eiriksson     """

print("Welcome to car rentals!")
Response = str(input("Would you like to continue (y/n)? "))

while Response == "y":
    
    Code = str(input("Customer code (b or d): "))
    Days = int(input("Number of days: "))
    Odo_start = int(input("Odometer reading at the start: "))
    Odo_end = int(input("Odometer reading at the end: ")) 

    Mileage = Odo_end - Odo_start   # Miles driven

    if Code == "b":     # Budget option
        Base_charge = 40 * Days
        Mileage_charge = 0.25 * Mileage
        
    elif Code == "d":       # Daily option
        Base_charge = 60 * Days

        if Mileage > (Days * 100):      # If driven more than 100km p/day on avg
            Mileage_charge = (Mileage - (Days * 100)) * 0.25
        else:
            Mileage_charge = 0          # If driven less than 100km p/day on avg

        
    Price = round(float(Base_charge + Mileage_charge),1)
            # Total amount rounded to 1 one decimal digit

    print("Miles driven:",Mileage)
    print("Amount due:",Price)

    Response = str(input("Would you like to continue (y/n)? "))