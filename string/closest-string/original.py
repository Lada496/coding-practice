#User function Template for python3

class Solution:
    def shortestDistance(self, s, word1, word2):
	    # code here
	    i1 = 0
	    i2 = 0
	    distance = len(s)
	    for i in range(len(s)):
		    if s[i] == word1:
		        i1 = i
		        for j in range(i, len(s)):
		            if s[j] == word1:
		                i1 = j
		            if s[j] == word2:
		                i2 = j
		                distance = min(distance, i2 - i1)
		    elif s[i] == word2:
		        i1 = i
		        for j in range(i, len(s)):
		            if s[j] == word2:
		                i1 = j
		            if s[j] == word1:
		                i2 = j
		                distance = min(distance, i2 - i1)
		 
    return distance