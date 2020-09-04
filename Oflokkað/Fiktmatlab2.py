from os import system
import math
import sympy as sym
import matplotlib.pyplot as plt
system("clear")

x = sym.symbols("x")
Area = float(10)
Area = [-Area, Area]
h = x - sym.cos( x ** 2 )
plot1 = sym.plot(h,line_color = "purple", show = False)
plot2 = sym.plot(x,line_color = "red", show = False)
plot1.append(plot2[0])
plot1.xlim = Area
plot1.ylim = Area
plot1.xlabel = "$x - cos(x^2)$"
plot1.title = "Math project"

plot1.save("Óflokkað/mynd11")
plot1.show()


