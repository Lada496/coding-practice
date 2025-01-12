class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        arr.sort()
        first = arr[0]
        last = arr[-1]
        
        ans = ""
        i = 0
        
        while i < len(first) and i < len(last):
            if first[i] == last[i]:
                ans += first[i]
                i += 1
            else:
                break
        
        return ans