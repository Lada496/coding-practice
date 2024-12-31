# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s:int, e:int) -> List[Pair]:

        # When the length is 1
        if e - s <= 0:
            return pairs
        
        m = (s + e) // 2

        self.mergeSortHelper(pairs, s, m)

        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs

    
    def merge(self, arr: List[Pair], s: int, m: int, e:int) -> None:

        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i, j, k = 0, 0, s

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
