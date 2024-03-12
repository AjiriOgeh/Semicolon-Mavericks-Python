import sys

import seven_segments_display


def seven_segments_app():
    user_input = input("Enter input to display a character: ")
    try:
        print(seven_segments_display.display_seven_segment(user_input))
        sys.exit(1000)
    except ValueError as error:
        print(f"{error}")
        print()
        seven_segments_app()


seven_segments_app()
