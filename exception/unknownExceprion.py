# Python code to illustrate working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except Exception as e:
		print("Sorry ! You are dividing by zero ")
		print(e)

# Look at parameters and note the working of Program
divide(3, 0)
divide(3, 2)