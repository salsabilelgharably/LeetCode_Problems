class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        mon = 1
        count = 1
        for i in range(n):
            if count - mon == 7:
                mon += 1
                count = mon
            res += count
            count += 1
        return res    
            
        