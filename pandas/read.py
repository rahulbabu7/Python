# import  pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# usecols = ['name','physics']  #!for printing this 2 colums
# df = pd.read_csv("EXAMresult.csv",index_col=0)

# print(df)
# plt.plot(df['maths'],df['REGNO'],marker= "o")
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('EXAMresult.csv')

# Draw a plot of the weather report with date as the x-axis and temperature as the y-axis
plt.plot(df['REGNO'], df['maths'], marker='o')


# Show the plot
plt.show()
