class Solution:
    def arrangeCoins(self, n: int) -> int:
        left= 0
        right= n
        while left <=  right:
            mid= int((left+right)/2)
            if (mid*(mid+1))/2 < n:
                left= mid +1
            elif (mid*(mid+1))/2 > n:
                right= mid -1
            else: 
                return mid
            
        return left-1
        