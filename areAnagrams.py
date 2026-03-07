from collections import Counter
class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       a = Counter(s1)
       b = Counter(s2)
       return a == b
       