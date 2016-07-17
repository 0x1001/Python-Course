import unittest


def insertion_sort(data):
    sorted_data = [i for i in data]
    for i in range(1, len(sorted_data)):
        num = sorted_data[i]
        j = i
        while j > 0 and sorted_data[j - 1] > num:
            sorted_data[j] = sorted_data[j - 1]
            j -= 1
        sorted_data[j] = num
    return sorted_data


def merge_sort(data):
    if len(data) == 1:
        return data
    elif len(data) == 0:
        return []

    new_data = [i for i in data]
    half_index = int(len(new_data) / 2)
    left_part = new_data[0:half_index]
    right_part = new_data[half_index:len(new_data)]

    sorted_data = []

    # Sort half lists
    left_sorted = merge_sort(left_part)
    right_sorted = merge_sort(right_part)

    # Merge lists
    while len(left_sorted) != 0 and len(right_sorted) != 0:
        if left_sorted[0] <= right_sorted[0]:
            sorted_data.append(left_sorted.pop(0))
        else:
            sorted_data.append(right_sorted.pop(0))

    while len(left_sorted) != 0:
            sorted_data.append(left_sorted.pop(0))

    while len(right_sorted) != 0:
            sorted_data.append(right_sorted.pop(0))

    return sorted_data

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_6"))
