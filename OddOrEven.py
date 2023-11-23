number = int(input("Enter a number: "))

remainder = number % 2

if remainder == 0:
	print(number,"is an even number")

if remainder != 0:
	print(number,"is an odd number")