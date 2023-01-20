class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsets, non_decreasing_subseq = [[]], []
        for i in range(len(nums)):
            for j in range(len(subsets)):
                subset = subsets[j] + [nums[i]]
                subsets.append(subset)
                if len(subset) > 1 and subset not in non_decreasing_subseq and subset == sorted(subset):
                    non_decreasing_subseq.append(subset)
        return non_decreasing_subseq