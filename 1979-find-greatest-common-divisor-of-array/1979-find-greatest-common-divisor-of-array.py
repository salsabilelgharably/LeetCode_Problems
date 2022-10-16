class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        min_num = min(nums)
        counter = min_num
        while counter >= 1:
            if max_num % counter == 0 and min_num % counter == 0:
                return counter
            counter -= 1
        