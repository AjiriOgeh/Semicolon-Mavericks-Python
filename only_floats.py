def only_floats(number_one, number_two):
	if type(number_one) == float and type(number_two) == float:
		return 2

	elif type(number_one) == float or type (number_two) == float:
		return 1
	
	else:
		return 0
