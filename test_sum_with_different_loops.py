import sum_with_different_loops

def test_sum_with_while_loop_one():
	assert sum_with_different_loops.sum_with_while_loop([1, 2, 3, 4, 5]) == "The total of the numbers in the list with while loop is 15"

def test_sum_with_while_loop_two():
	assert sum_with_different_loops.sum_with_while_loop([3, 6, 9, 12, 15]) == "The total of the numbers in the list with while loop is 45"

def test_sum_with_while_loop_negative_numbers():
	assert sum_with_different_loops.sum_with_while_loop([-8, -7, -6, -5]) == "The total of the numbers in the list with while loop is -26"

def test_sum_with_for_loop_integers():
	assert sum_with_different_loops.sum_with_for_loop([25, 50, 75, 100]) == "The total of the numbers in the list with for loop is 250"

def test_sum_with_for_loop_floats():
	assert sum_with_different_loops.sum_with_for_loop([0.75, 0.23, 0.14]) == "The total of the numbers in the list with for loop is 1.12"

