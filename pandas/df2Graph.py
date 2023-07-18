import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("topper.csv",index_col=1)
print(data)

plt.title("mapping")
plt.xlabel("regno")
plt.ylabel("cgpa")
plt.scatter(data['RegNo'],data['cgpa'])

plt.show()