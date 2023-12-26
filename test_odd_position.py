import odd_position

def test_odd_position_one():
	assert odd_position.odd_position([0,1,2,3,4,5]) == [1,3,5]

def test_odd_position_two():
	assert odd_position.odd_position([0.22, 0.33, 0.44, 0.55, 0.66, 0.77]) == [0.33, 0.55, 0.77]

def test_odd_position_countries():
	assert odd_position.odd_position(["Argentina", "Brazil", "Chile", "Denmark", "Ethiopia", "Finland"]) == ["Brazil", "Denmark", "Finland"]

def test_odd_position_boolean():
	assert odd_position.odd_position([True, False, True, False, True, False]) == [False, False, False]