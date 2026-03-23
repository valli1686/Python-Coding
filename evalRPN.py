class Solution(object):
    def evalRPN(self, tokens):
        s=[]
        for t in tokens:
            if t not in "+-/*":
                s.append(int(t))
            else:
                r,l = s.pop(), s.pop()
                if t == "+":
                    s.append(r+l)
                elif t == "-":
                    s.append(l-r)
                elif t == "*":
                    s.append(l*r)
                else:
                    s.append(int(float(l)/r))
        return s.pop()
        