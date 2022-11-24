class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while end >= start:
            middle = int((start + end)/2)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                if nums[middle-1] < target or middle == 0:
                    return middle
                else:
                    end = middle -1
            else:
                if middle == len(nums)-1 or nums[middle+1] > target:
                    return middle + 1
                else:
                    start = middle+1