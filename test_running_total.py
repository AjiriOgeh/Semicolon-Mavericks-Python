import running_total

def test_running_total_intergers_one():
	assert running_total.running_total([2, 4, 6, 8, 10]) == 30

def test_running_total_integers_two():
	assert running_total.running_total([1, 2, 3, 4, 5]) == 15

def test_running_total_negative_numbers():
	assert running_total.running_total([-3, -8, -12, -54, - 60, -150]) == -287

