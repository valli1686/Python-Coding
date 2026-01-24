class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=str(n)
        for i in range(len(n)-3, 0, -3):
            n=str(n)[:i] + "." + str(n)[i:]
        return n