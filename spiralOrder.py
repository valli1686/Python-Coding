class Solution(object):
    def spiralOrder(self, matrix):
        t,b = 0,len(matrix)-1
        l,r= 0, len(matrix[0])-1
        lst=[]
        while t<=b and l <= r:
            for i in range(l,r+1):
                lst.append(matrix[t][i])
            t += 1
            for i in range(t,b+1):
                lst.append(matrix[i][r])
            r -= 1
            if t<=b:
                for i in range(r,l-1,-1):
                    lst.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b,t-1,-1):
                    lst.append(matrix[i][l])
                l += 1
        return lst
        