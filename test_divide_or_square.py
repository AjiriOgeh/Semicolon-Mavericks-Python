import divide_or_square

def test_divide_or_square_for_not_mulitiple_of_five():
	assert divide_or_square.divide_or_square(21)==1

def test_divide_or_square_for_multiple_of_five():
	assert divide_or_square.divide_or_square(625)==25

def test_divide_or_square_for_not_mulitiple_of_five_with_wrong_assertion():
	assert divide_or_square.divide_or_square(34)==1

def test_divide_or_square_for_multiple_of_five_with_wrong_assertion():
	assert divide_or_square.divide_or_square(100)==8




