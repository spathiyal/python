def binarySearch(nums, target, searchFirst):

    (left, right) = (0, len(nums) - 1)

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            result = mid

            if searchFirst:
                right = mid - 1

            else:
                left = mid + 1

        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return result


arr = [2, 5, 5, 5, 5, 5, 8, 9, 9, 9]
n = 19


def sortedFrequency(arr, n):

    # pass true for the first occurrence
    first = binarySearch(arr, n, True)
    # pass false for the last occurrence
    last = binarySearch(arr, n, False)

    count = last - first + 1

    if first != -1:
        return count
    else:
        return -1


print(sortedFrequency(arr, n))
