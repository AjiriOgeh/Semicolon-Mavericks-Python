import number_split_to_digits

def test_number_split_to_digits_one():
	assert number_split_to_digits.number_split_to_digits(75) == [7, 5]

def test_number_split_to_digits_two():
	assert number_split_to_digits.number_split_to_digits(648) == [6, 4, 8]

def test_number_split_to_digits_three():
	assert number_split_to_digits.number_split_to_digits(2970) == [2, 9, 7, 0]

def test_number_split_to_digits_four():
	assert number_split_to_digits.number_split_to_digits(12345) == [1, 2, 3, 4, 5]

