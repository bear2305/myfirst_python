print("\n Select what you want to calulate in LC Circuit :\n")
print("\n 1. Frequency(F)  2. Inductance(L)  3. Capacitance(C)\n")

Q = input("Input Selected Option :  ").lower()

if Q in ["1", "frequency", "f", "one", "hz", "hertz"]:
	try:
		print("\n To Calculate the Frequency of the LC Circuit\n")
		print("")
		l = float(input(' Input the Inductance value :  '))
		c = float(input(' Input the Capacitance value :  '))
		print("")
		if l <= 0 or c <= 0:
			raise ZeroDivisionError
		d = 44 * (l ** 0.5) * (c ** 0.5)
		f = 7 / d
		print(f"\n The Resulting Frequency = {f} Hz\n")
	except ValueError:
		print("\nInvalid input; Only numbers\n")
	except ZeroDivisionError:
		print("\nInductance and Capacitance must be greater than zero!\n")
elif Q in ["2", "inductance", "i", "l", "two", "h", "henry"]:
	try:
		print("\nTo Calculate the Inductance needed for the LC circuit \n")
		print("")
		f = float(input(' Input the Frequency value :  '))
		c = float(input(' Input the Capacitance value :  '))
		print("")
		if f <= 0 or c <= 0:
			raise ZeroDivisionError
		d = 1936 * c * (f ** 2)
		l = 49 / d
		print(f"\n The Inductance needed = {l} H \n")
	except ValueError:
		print("\n Invalid input; Only numbers!!! \n ")
	except ZeroDivisionError:
		print("\nFrequency and Capacitance must be greater than zero!\n")

elif Q in ["3", "capacitance", "three", "c", "farad"]:
	try:
		print("\n To Calculate the Capacitance needed in the LC circuit \n")
		print("")
		f = float(input(" Input the Frequency value :  "))
		l = float(input(" Input the Inductance value:  "))
		print("")
		if f <= 0 or l <= 0:
			raise ZeroDivisionError
		d = 1936 * l * (f ** 2)
		c = 49 / d
		print(f"\n The Capacitance needed : {c} F \n")
	except ValueError:
		print("\n Invalid input; Only numbers!!! \n")
	except ZeroDivisionError:
		print("\nFrequency and Inductance must be greater than zero!\n")

else:
	print("\n Invalid input; try again!!! \n")
