def sequential_list():
    numbers = []
    for number in range(1, 16):
        numbers.append(number)
    return numbers


def duplicate_sequential_list(numbers):
    new_list = numbers * 2
    return new_list


def eliminate_duplicate_values_in_list(numbers):
    numbers = list(set(numbers))
    return numbers


def add_every_third_element_in_list(numbers):
    total = 0
    for number in numbers[2::3]:
        total += number
        print(total)
    return total


def add_first_middle_last_element_in_list(numbers):
    if len(numbers) % 2 == 0:
        middle_element = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
        total = numbers[0] + middle_element + numbers[-1]

    else:
        middle = len(numbers) // 2
        total = numbers[0] + numbers[middle] + numbers[-1]
    return total

