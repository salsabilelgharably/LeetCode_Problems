class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        length = 1
        max_len = 1
        if len(nums) == 0:
            return 0 
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                length += 1
                max_len = max(length , max_len)
            else:
                length = 1
        return max_len   
        