class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            rem = target - nums[i]
            
            if rem in seen:
                return [i, seen[rem]]
            else:
                seen[num] = i