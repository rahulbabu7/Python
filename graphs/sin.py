import matplotlib.pyplot as plt
import numpy as np
import math

x= np.arange(0,math.pi*2)  #!range for x
y = np.sin(x) #!sin function
plt.plot(x,y)
plt.xlabel("values")
plt.ylabel("sin")
plt.show()