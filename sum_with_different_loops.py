def sum_with_while_loop(number_list):
	total = 0
	index = 0
	count = 0
	while count < len(number_list):
		total += number_list[index]
		count += 1
		index += 1
	return f"The total of the numbers in the list with while loop is {total}"

def sum_with_for_loop(number_list):
	total = 0
	for number in number_list:
		total += number
	return f"The total of the numbers in the list with for loop is {total}"