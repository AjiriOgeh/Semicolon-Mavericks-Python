number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

sum = number1 + number2 + number3
product = number1 * number2 * number3
average = (number1 + number2 + number3) / 3

print("The sum of the numbers is", sum)
print("The product of the numbers is", product)
print(f"The average of the numbers is {average:.2f}")

if number1 < number2 and number1 < number3:
	print(number1,"is the smallest number")

if number2 < number1 and number2 < number3:
	print(number2,"is the smallest number")

if number3 < number1 and number3 < number2:
	print(number3,"is the smallest number")

if number1 > number2 and number1 > number3:
	print(number1,"is the largest number")

if number2 > number1 and number2 > number3:
	print(number2,"is the largest number")

if number3 > number1 and number3 > number2:
	print(number3,"is the largest number")