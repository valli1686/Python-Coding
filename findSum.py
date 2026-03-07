class Solution:
	def findSum(self, s1, s2):
		# code here
		s=""
		l = max(len(s1),len(s2))
		s1 = s1[::-1]
		s2 = s2[::-1]
		res = []
		c = 0
		for i in range(l):
		    a = int(s1[i]) if i < len(s1) else 0
		    b = int(s2[i]) if i < len(s2) else 0
		    
		    t = a+b+c
		    res.append(str(t%10))
		    c = t // 10
		if c:
		    res.append(str(c))
		final = "".join(res[::-1])
		final = final.lstrip('0')
		
		return final if final else '0'
		    