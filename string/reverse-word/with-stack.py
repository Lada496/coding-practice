
class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # code here 
        stack = []
        word = ""
        ans = ""
        
        for char in s:
            if char != " ":
                word += char
            elif word:
                stack.append(word)
                word = ""
        
        if word:
            stack.append(word)
        
        i = 0
        last = len(stack) - 1
        while stack:
            if i == last:
                ans += stack.pop()
            else:
                ans += stack.pop() + " "
            i += 1
        
        return ans