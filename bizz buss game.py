while True:
	def fizzbuzz(x):
		if x%3 == 0 and x%5 == 0 :
			return print("fizzbuzz")
		if x%3 ==0:
			return print("fizz")
		if x%5 ==0:
			return print("buzz")
		return print(x)
	x= int(input("number :  "))
	fizzbuzz(x)
	
	
	