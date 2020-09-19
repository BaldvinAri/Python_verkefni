import matplotlib.pyplot as plt
import math
import numpy as num

mes = num.linspace(0, 2 * math.pi, 100)

x_cords = num.cos(mes) + num.sin(mes)

figure = plt.figure(figsize=(7,7))

plt.plot(x_cords,y_cords)

plt.show()