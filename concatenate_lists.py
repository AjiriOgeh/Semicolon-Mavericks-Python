def concatenate_lists(first_list, second_list):
	second_list_index = 0
	for item in second_list:
		first_list.append(second_list[second_list_index])
		second_list_index += 1
	return first_list