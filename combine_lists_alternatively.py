def combine_lists_alternatively(first_list, second_list):
	first_list_index = 0
	second_list_index = 0
	new_list = []	

	for item in first_list:
		new_list.append(first_list[first_list_index])
		new_list.append(second_list[second_list_index])
		
		first_list_index += 1
		second_list_index += 1	
		
	return new_list

print(combine_lists_alternatively([1,2,3,4],[7,8,9,10]))