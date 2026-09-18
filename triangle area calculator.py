def repeat():
	loop=True
	while loop:
		global try_again
		print("")
		repeat = input("Enter 1 to calculate again or 2 to Cancel :  ")
		if repeat == "1":
			try_again = True
			loop=False
		elif repeat == "2":
			try_again=False
			loop=False
		else:
			print("")
			print("Enter only number, 1 or 2")
			print("")
			loop=True
			
try_again=True
while try_again:
		try:
			print("")
			base=float(input("Base Dimension : "))
			if base<=0:
				print("Invalid Base Dimension")
				print("")
			else:
				height=float(input("Height Dimension : "))
				if height<=0:
					print("Invalid Height Dimension")
					print("")
				else:
					result = 0.5*base*height
					print("Area of the triangle is : ",result,"units")
					print("")
					repeat()
					
		except ValueError:
			print("")
			print("Type only numbers")
			print("")
			try_again = True