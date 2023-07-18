import matplotlib.pyplot as plt
import numpy as np
year = np.array([2020,2019,2018])
values = np.array([1,2,3])
plt.xlabel("year")
plt.ylabel("values")
# plt.plot(year,values,'r-o',label = "yearage")
# plt.plot(year,values,'r--',label = "yearage")
plt.plot(year,values,'r o',label = "yearage")
plt.legend()
plt.show()