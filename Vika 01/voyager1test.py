d_str = input('Number of days after 9/25/09?')
d_int = int(d_str)
m = 16637000000
v = 38241 * 24 * d_int
km = 1.609344
v_AU = 92955887.6
M = m + v
k = M * km
AU = (m + v)/v_AU
M_rnd = round(M)
k_rnd = round(k)
AU_rnd = round(AU)

 

print("Number of days after 9/25/09:", d_int)
print("Miles from the sun:", M_rnd)
print("kilometers from the sun:", k_rnd)
print("AU from the sun:", AU_rnd)
