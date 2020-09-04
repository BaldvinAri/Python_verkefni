# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import math as m

Dots = np.linspace(0, 2 * m.pi , 100)
x_cords = np.cos(Dots)
y_cords = np.sin(Dots)
figure = plt.figure(figsize=(7,7))

plt.plot( x_cords , y_cords , label = "Cos(x) vs Sin(x)")
plt.legend("Hringur")

plt.savefig("Óflokkað/Hringurprufa", transparent = True)
plt.show()

