import combine_lists_alternatively

def test_combine_lists_alternatively_integers():
	assert combine_lists_alternatively.combine_lists_alternatively([1, 3, 5, 7 ,9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_combine_lists_alternatively_letters_and_numbers():
	assert combine_lists_alternatively.combine_lists_alternatively(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]

def test_combine_list_alternatively_animals():
	assert combine_lists_alternatively.combine_lists_alternatively(["Antelope", "Cat", "Elephant", "Goat"], ["Bat", "Dog", "Fox", "Horse"]) == ["Antelope", "Bat", "Cat", "Dog", "Elephant", "Fox", "Goat", "Horse"]

