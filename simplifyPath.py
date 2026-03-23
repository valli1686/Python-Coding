class Solution(object):
    def simplifyPath(self, path):
        l=[]
        path = path.split('/')
        for i in path:
            if i == '':
                continue
            elif i == '..':
                if l:
                    l.pop()
            elif i == '.':
                continue
            else:
                l.append(i)
        return '/'+'/'.join(l)
        