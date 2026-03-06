#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		c=0
		while n > 0:
		    n = n & (n-1)
		    c += 1
		return c