def add(a,b):
	print(f"ADDING {a} + {b}")
	return a+b

def substract(a,b):
	print(f"SUBSTRACTING {a} - {b}")
	return a-b

def multiply(a,b):
	print(f"MULTIPLYING {a} * {b}")
	return a*b

def divide(a,b):
	print(f"Dividing {a} / {b}")
	return a/b

print("LEt's do some math with just functions!")

age=add(30,5)
height=substract(78,4)
weight=multiply(90,3)
iq=divide(100,1)

print(f"Age: {age}, HEight: {height},Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")
what=add(age,substract(height,multiply(weight,divide(iq,2))))

print("That becomes:",what,"Can you do it by hand?")