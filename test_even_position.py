import even_position

def test_even_position():
	assert even_position.even_position([10, 20, 30, 40, 50, 60]) == [10, 30, 50]

def test_even_position_animals():
	assert even_position.even_position(["Antelope", "Blue whale", "Cheetah", "Dog", "Eagle"]) == ["Antelope", "Cheetah", "Eagle"]


def test_even_position_boolean():
	assert even_position.even_position([True, False, True, False, True, False]) == [True, True, True]