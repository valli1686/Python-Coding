class Solution(object):
    def check(self, nums):
        for i in range(0,len(nums)):
            if nums[i-1] > nums[i]:
                for j in range(i+1,len(nums)):
                    if nums[j] < nums[j-1]:
                        return False
        return True
        