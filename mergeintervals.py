class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals)
        l=[]
        i = 0
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            while i+1 < len(intervals) and intervals[i+1][0] <= e:
                i += 1
                e = max(e, intervals[i][1])
            l.append([s,e])
            i += 1
        return l