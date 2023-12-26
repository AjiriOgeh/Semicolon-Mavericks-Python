def largest_element(numbers_list):
	largest_number = numbers_list[0]
	for number in numbers_list:
		if number > largest_number:
			largest_number = number
	return largest_number
