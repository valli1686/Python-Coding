class Solution(object):
    def summaryRanges(self, nums):
        a=[]
        i=0
        while i < len(nums):
            s = i
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            if i != s:
                a.append(str(nums[s])+'->'+str(nums[i]))
            else:
                a.append(str(nums[i]))
            i += 1
        return a       
        