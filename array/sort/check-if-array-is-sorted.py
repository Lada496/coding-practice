#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < prev:
                return False
            prev = arr[i]
        
        return True
            