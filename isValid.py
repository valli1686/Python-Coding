class Solution(object):
    def isValid(self, s):
        a = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                a.append(i)
            elif i == ')' and a and a[-1] == '(':
                a.pop()
            elif i == ']' and a and a[-1] == '[':
                a.pop()
            elif i == '}' and a and a[-1] == '{':
                a.pop()
            else:
                return False
        return len(a) == 0