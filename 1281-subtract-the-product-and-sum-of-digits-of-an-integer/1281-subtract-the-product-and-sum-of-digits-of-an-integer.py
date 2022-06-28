class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum_n = 0
        for i in str(n):
            x = int(i)
            product *= x
            sum_n += x
        return product - sum_n 