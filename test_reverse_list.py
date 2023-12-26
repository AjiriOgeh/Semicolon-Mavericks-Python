import reverse_list

def test_reverse_list_integers():
	assert reverse_list.reverse_list([13, 25, 37, 49, 52]) == [52, 49, 37, 25, 13]

def test_reverse_list_string():
	assert reverse_list.reverse_list(["Manchester United", "Chelsea", "Liverpool", "Arsenal", "Tottenham"]) == (["Tottenham", "Arsenal", "Liverpool", "Chelsea", "Manchester United"])
		
def test_reverse_list_mixed_data_types():
	assert reverse_list.reverse_list([0.85, "Book", 500, True, 'A', [1,2,3]]) == ([[1,2,3], 'A', True, 500, "Book", 0.85]) 