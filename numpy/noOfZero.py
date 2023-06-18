import numpy as np

def noOfZero(arr):
    count = np.count_nonzero(arr)
    return count
array = np.array([[0,10,20],[20,30,40]])

print("Orginal array = ")
print(array)

result = noOfZero(array)
print("Total number of NonZero = ",result)
