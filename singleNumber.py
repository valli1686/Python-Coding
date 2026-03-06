class Solution(object):
    def singleNumber(self, nums):
        n=0
        for i in nums:
            n = n^i
        vb = n & (-n)
        x,y = 0,0
        for num in nums:
            if(num & vb == 0):
                x = x^ num
            else:
                y = y^num
        
        return [x,y]

        