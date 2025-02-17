class Solution:   
    def peakElement(self,arr):
        # Code here
        for i in range(len(arr)):
            if i + 1 <= len(arr) - 1 and i - 1 >= 0 and arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i
            if i == len(arr) - 2 and arr[i] < arr[i + 1]:
                return i + 1
                
        return False
