number = int(input("Enter integer with five digits: "))

digit5 = number % 10
quotient1 = number // 10

digit4 = quotient1 % 10
quotient2 = quotient1 // 10

digit3 = quotient2 % 10
quotient3 = quotient2 // 10

digit2 = quotient3 % 10
quotient4 = quotient3 // 10

digit1 = quotient4 % 10
quotient5 = quotient4 // 10

print(digit1,"   ", digit2,"   ", digit3,"   ", digit4,"   ", digit5,"   ")