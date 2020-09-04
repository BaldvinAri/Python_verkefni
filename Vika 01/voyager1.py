d0_miles = 16637000000
    # Distance from sun day 0 in miles
vpHour_miles = 38241
    # Speed of Voyager in miles per hour
vpDay_miles = 38241 * 24
    # Speed of Voyager in miles per day
MilesToKm = 1.609344
    # Km per mile
d0_km = MilesToKm * d0_miles
    # Distance from sun day 0 in km
vpHour_km = MilesToKm * vpHour_miles
    # Speed of Voyager in km per hour
vpDay_km = MilesToKm * vpDay_miles
    # Speed of Voyager in km per day
AU_to_miles = 92955887.6
    # 1 Astronomical unit in miles


Days_int = int(input("Number of days after 9/25/09: "))
    # User input
    

MilesFromSun = d0_miles + (Days_int * vpDay_miles)
    # Distance from sun on dayX in miles
KmFromSun = round(d0_km + (Days_int * vpDay_km))
    # Distance from sun on dayX in km, rounded
AUFromSun = round(MilesFromSun / AU_to_miles)
    # Distance from sun on dayX in Astronomical units, rounded

if Days_int < 0:
    print("Unknown")

if Days_int >= 0:
    print("Miles from the sun:", MilesFromSun)
    print("Kilometers from the sun:", KmFromSun)
    print("AU from the sun:", AUFromSun)
