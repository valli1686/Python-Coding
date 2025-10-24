class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            a=[0] * (len(s)-1)
            for i in range(0,len(s)-1):
                a[i] = (int(s[i]) + int(s[i+1])) % 10
            s = ''.join(str(x) for x in a)
        if s[0] == s[1]:
            return True
        else:
            return False
        