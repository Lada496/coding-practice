class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # code here 
        arr = s.split(" ")
        filtered = list(filter(lambda s: s != "", arr))
        reverse = filtered[::-1]
        return (" ").join(reverse)