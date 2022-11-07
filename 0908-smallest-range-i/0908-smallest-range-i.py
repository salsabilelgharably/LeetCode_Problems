class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mi = min(nums)+k
        mx = max(nums)-k
        if mi >= mx:
            return 0
        
        return mx-mi