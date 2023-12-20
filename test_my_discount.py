import my_discount

def test_my_discount_correct_assertion():
	assert my_discount.my_discount(150, 15)==127.5

def test_my_discount_correct_assertion_second():
	assert my_discount.my_discount(7500, 20)==6000


def test_my_discount_wrong_assertion():
	assert my_discount.my_discount(100, 10)==55