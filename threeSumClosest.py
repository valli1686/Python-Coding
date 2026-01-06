class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        ans = 0

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(target - s) < res:
                    res = abs(target - s)
                    ans = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s  

        return ans
