import unittest


def insertion_sort(data):
    sorted_data = data[:]

    for i in range(1, len(sorted_data)):
        while i > 0 and sorted_data[i - 1] > sorted_data[i]:
            sorted_data[i], sorted_data[i - 1] = sorted_data[i - 1], sorted_data[i]
            i -= 1

    return sorted_data


def merge_sort(data):
    if len(data) == 1:
        return data[:]
    elif len(data) == 0:
        return []

    half_index = int(len(data) / 2)
    left_part = data[:half_index]
    right_part = data[half_index:]

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

    sorted_data.extend(left_sorted)
    sorted_data.extend(right_sorted)

    return sorted_data

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_6"))
