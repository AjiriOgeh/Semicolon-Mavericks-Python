items = set()
for value in range(1, 10):
    item = int(input("Enter a number: "))
    items.add(item)
print(items)


def sum_collection(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def remove_item(element, numbers):
    if element in numbers:
        numbers.remove(element)
        return element
    else:
        return None


def find_intersection(first_set, second_set):
    return first_set & second_set


values = {1, 2, 3, 4, 5, 6}
cars = {1, 2, 3, 4, 5, 8, 9, 10}
# print(sum_collection(numbers))

print(remove_item(19, cars))
