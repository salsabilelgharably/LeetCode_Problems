class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        nums = [0,1]
        for i in range(1, n):
            nums.append(nums[-1] + nums[-2])
        
        
        return nums[n]