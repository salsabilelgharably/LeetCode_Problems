class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]