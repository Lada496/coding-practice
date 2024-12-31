# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
    
    def quickSortHelper(self, pairs, s, e) -> List[Pair]:
        
        if e - s <= 0:
            return pairs

        pivot = pairs[e]

        smaller = s
        i = s
        while i <= e:
            if pairs[i].key < pivot.key:
                tmp = pairs[smaller]
                pairs[smaller] = pairs[i]
                pairs[i] = tmp
                smaller += 1
            i += 1
        #left = pairs[: smaller]
        #right = pairs[smaller + 1:]

        tmp = pairs[smaller]
        pairs[smaller] = pivot
        pairs[e] = tmp

        self.quickSortHelper(pairs, s, smaller - 1)
        self.quickSortHelper(pairs, smaller + 1, e)

        return pairs



## Better solution
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    # Implementation of Quick Sort
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return

        pivot = arr[e] # pivot is the last element
        left = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot
        
        # Quick sort left side
        self.quickSortHelper(arr, s, left - 1)

        # Quick sort right side
        self.quickSortHelper(arr, left + 1, e)