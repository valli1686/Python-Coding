class Solution(object):
    def insert(self, intervals, newInterval):
        l=[]
        
        if not intervals:
            return [newInterval]

        i = 0
        inserted = False

        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]

            if newInterval[0] <= e and newInterval[1] >= s:
                s = min(s, newInterval[0])
                e = max(e, newInterval[1])
                inserted = True

            while i+1 < len(intervals) and intervals[i+1][0] <= e:
                i += 1
                e = max(e, intervals[i][1])

            l.append([s,e])
            i += 1
        
        if not inserted:
            l.append(newInterval)

        return sorted(l)