def reverse_list(items_list):
	new_index = -1
	new_list = []
	for items in items_list:
		new_list.append(items_list[new_index])
		new_index = new_index - 1
				
	return new_list