
print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    # REQ-04: Return 0 if list is empty
    if n == 0:
        return 0

    # REQ-03: Return 1 if list has 10 or more elements
    if n >= 10:
        return 1

    # REQ-05: Return 2 if any element is not an integer
    for num in arr_result:
        if not isinstance(num, int):
            return 2

    # REQ-01 & REQ-02: Bubble sort
    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array for invalid sorting order
                    return []

    return arr_result


def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)


if __name__ == "__main__":
    main()
