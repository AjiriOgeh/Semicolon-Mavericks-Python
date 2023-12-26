import largest_element

def test_largest_element_integers_one():
	assert largest_element.largest_element([1, 2, 3, 4, 5]) == 5

def test_largest_element_two_integers_two():	
	assert largest_element.largest_element([125, 25000, 50, 5, 1000]) == 25000

def test_largest_element_floats():
	assert largest_element.largest_element([0.75, 12.5, 87.5, 1.5, 22.5, 39.5, 62.5]) == 87.5

def test_largest_element_negative_numbers():
	assert largest_element.largest_element([-1, -45, -23, -37, -150, -9]) == -1

def test_largest_element_different_numeric_types():
	assert largest_element.largest_element([0.35, - 7, -4.5, 1, 160, -0.879, 450.05, -25]) == 450.05