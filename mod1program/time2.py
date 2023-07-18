sec = int(input("Enter the time in result"))

min = sec//60

hr  = sec//(60**2)
secnd  = sec%60
mins = min%60

print(f"{hr}H:{mins}M:{secnd}S")