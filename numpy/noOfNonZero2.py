import numpy as np
arr = np.array([[0,10,20],[20,30,40]])
count=0
for i in arr:
    for j in i:
        if not j==0:
            count = count+1
print(count)