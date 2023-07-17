def summation(low, high):
    total = 0
    for num in range(low, high + 1):
        total += num
    return total


result = summation(1, 10)
print(result) 
