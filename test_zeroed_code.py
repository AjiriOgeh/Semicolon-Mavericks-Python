import zeroed_code

def test_zeroed_code():
	assert zeroed_code.zeroed_code([1,2,3,4,5])==[0,2,3,4,0]

def test_zeroed_code_second():
	assert zeroed_code.zeroed_code([78,67,32,8,345,122,564])==[0,67,32,8,345,122,0]

def test_zeroed_code_third():
	assert zeroed_code.zeroed_code([124, 63, 945,18, 6832, 54])==[0, 63, 945,18, 6832, 0]
