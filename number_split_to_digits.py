def number_split_to_digits(number):
	cast_list = str(number)
	new_list = []

	for item in cast_list:
		new_list.append(int(item))
	return new_list