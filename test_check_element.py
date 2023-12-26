import check_element

def test_check_element_fruits():
	assert check_element.check_element("apple", ["banana", "pineapple", "orange", "lemon", "apple"]) == "The element apple exists in the list"

def test_check_element_numbers():
	assert check_element.check_element(3.75, [2, 3, 5, 7, 11]) == "The element 3.75 does not exist in the list"

def test_check_element_integers():
	assert check_element.check_element(150, [15, 250, 85, 150, 100]) == "The element 150 exists in the list"

def test_check_element_boolean_values():
	assert check_element.check_element(True, [False, False, False, False, False]) == "The element True does not exist in the list"

def test_check_element_different_data_types():
	assert check_element.check_element(10, ["Messi", 91, "Barcelona", 1.7, 10, "True"]) == "The element 10 exists in the list"

def test_check_element_food_products():
	assert check_element.check_element("fish", ["snails", "eggs", "chicken", "beef"]) == "The element fish does not exist in the list"