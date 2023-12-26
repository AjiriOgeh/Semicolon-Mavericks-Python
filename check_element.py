def check_element(element_to_check, items_list):
	if element_to_check in items_list:
		return f"The element {element_to_check} exists in the list"
	else:
		return f"The element {element_to_check} does not exist in the list"

