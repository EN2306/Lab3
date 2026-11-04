import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


# REQ-03: 10 or more numbers should return 1
def test_bubble_sort_ten_numbers():
    input_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 1


# REQ-04: Empty list should return 0
def test_bubble_sort_empty():
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 0


# REQ-05: Non-integer values should return 2
def test_bubble_sort_non_integer():
    input_arr = [64, 34, "abc", 12]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 2
