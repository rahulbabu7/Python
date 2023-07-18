import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("topper.csv")
print(data)
sorted = data.sort_values('cgpa',ascending=True)
print(sorted)
maz=data['cgpa'].max()
print(maz)
maxCgpa = data[['name','RegNo']][data.cgpa==maz]
print(maxCgpa) 

# plt.title("mapping")
# plt.xlabel("regno")
# plt.ylabel("cgpa")
# plt.scatter(data['RegNo'],data['cgpa'])

# plt.show()