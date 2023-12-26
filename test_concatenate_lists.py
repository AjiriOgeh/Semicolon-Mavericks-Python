import concatenate_lists

def test_concatenate_lists_different_data_types_one():
	assert concatenate_lists.concatenate_lists(["a", "b", "c"], [1, 2, 3]) == ["a", "b", "c", 1, 2, 3]

def test_concatenate_lists_different_data_types_two():
	assert concatenate_lists.concatenate_lists([1, 2, 3, 4], ["Chelsea", "Liverpool", "Arsenal", "Manchester United"]) == [1, 2, 3, 4, "Chelsea", "Liverpool", "Arsenal", "Manchester United"]

def test_concatenate_list_different_data_types_three():
	assert concatenate_lists.concatenate_lists(["Football", "Tennis", "Basketball", "Volleyball"],  [10.5, 22.5, 37.5, 48.5]) == ["Football", "Tennis", "Basketball", "Volleyball", 10.5, 22.5, 37.5, 48.5]