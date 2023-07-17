def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1

    return upper_count, lower_count


input_string = "Hello World"
upper, lower = count_upper_lower(input_string)
print("Uppercase count:", upper)  
print("Lowercase count:", lower) 
