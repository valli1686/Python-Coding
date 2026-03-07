class Solution:
    def checkPangram(self,s):
        #code here
        s = s.lower()
        s = set(ch for ch in s if ch.isalpha())
        return len(s) == 26
        
       