def display_mid_section():
    return "# # # #"


def display_right_side():
    return f"      # \n" \
           f"      #\n" \
           f"      #"


def display_left_side():
    return f"#    \n" \
           f"#    \n" \
           f"#      "


def display_both_sides():
    return f"#     #\n" \
           f"#     #\n" \
           f"#     #"


def user_input_to_list(user_input: str):
    user_input_list = []
    for character in user_input:
        user_input_list.append(character)
    return user_input_list


def display_segment_1(user_input: str):
    my_list = user_input_to_list(user_input)
    if my_list[0] == "1":
        return display_mid_section()


def display_segment_7(user_input: str):
    my_list = user_input_to_list(user_input)
    if my_list[6] == "1":
        return display_mid_section()


def display_segment_4(user_input: str):
    my_list = user_input_to_list(user_input)
    if my_list[3] == "1":
        return display_mid_section()


def display_either_segment_2_or_6(user_input: str):
    my_list = user_input_to_list(user_input)
    if my_list[1] == "1" and my_list[5] == "0":
        return display_right_side()
    if my_list[1] == "0" and my_list[5] == "1":
        return display_left_side()


def display_both_segment_2_and_6(user_input: str):
    my_list = user_input_to_list(user_input)
    if my_list[1] == "1" and my_list[5] == "1":
        return display_both_sides()


def display_both_segment_3_and_5(user_input: str):
    my_list = user_input_to_list(user_input)
    if my_list[2] == "1" and my_list[4] == "1":
        return display_both_sides()


def display_either_3_or_5(user_input: str):
    my_list = user_input_to_list(user_input)
    if my_list[2] == "1" and my_list[4] == "0":
        return display_right_side()
    if my_list[2] == "0" and my_list[4] == "1":
        return display_left_side()


def display_the_character(user_input: str):
    display_segment_1(user_input)
    display_both_segment_2_and_6(user_input)
    display_either_segment_2_or_6(user_input)
    display_segment_7(user_input)
    display_both_segment_3_and_5(user_input)
    display_either_3_or_5(user_input)
    display_segment_4(user_input)


def check_input_for_binary_digits(user_input: str):
    for binary_digit in user_input:
        if binary_digit not in '01':
            return False
    return True


def display_seven_segment(user_input: str):
    if len(user_input) != 8:
        raise ValueError("Input should only be eight characters")
    if not user_input.isdigit():
        raise ValueError("Input should only be numeric characters")
    if not check_input_for_binary_digits(user_input):
        raise ValueError("Input should contain only binary digits")
    if user_input[7] == "0":
        print(""" 
         
          
           
            
             
              
        """)
    else:
        return display_the_character(user_input)
