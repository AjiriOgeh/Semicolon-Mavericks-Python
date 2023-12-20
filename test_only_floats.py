import only_floats

def test_only_floats_all_floats():
	assert only_floats.only_floats(4.85, 99.99)==2

def test_only_floats_float_or_integer():
	assert only_floats.only_floats(2.75, 18)==1

def test_only_floats_integers():
	assert only_floats.only_floats(5, 6)==0

