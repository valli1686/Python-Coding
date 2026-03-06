class Solution(object):
    def minBitFlips(self, start, goal):
        a = start ^ goal
        c = 0
        while a > 0:
            a = a & (a-1)
            c += 1
        return c