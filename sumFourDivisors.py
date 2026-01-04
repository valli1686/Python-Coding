class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            div_sum,count = 0,0
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    count += 1
                    div_sum += i

                    if i != n // i:
                        count += 1
                        div_sum += n // i
            if count == 4:
                res += div_sum
        return res
        