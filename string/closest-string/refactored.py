#User function Template for python3

class Solution:
	def shortestDistance(self, s, word1, word2):
		# code here
		i1 = -1
		i2 = -1
		distance = 100000
		
		for i in range(len(s)):
		    if s[i] == word1:
		        i1 = i
		    if s[i] == word2:
		        i2 = i
		    if i1 != -1 and i2 != -1:
		        distance = min(distance, abs(i1 - i2))
		
	return distance