def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list


arr = [1, 2, 4, 9, 3, 5]
# [1, 2, 4] [9, 3, 5]
# [1, 2] [4] [9, 3] [5]
# [1] [2]    [9,3]

# [1, 2]     [3,9]
# [1, 2, 4]  [3, 5, 9]
# [1, 3, 4, 5, 9]