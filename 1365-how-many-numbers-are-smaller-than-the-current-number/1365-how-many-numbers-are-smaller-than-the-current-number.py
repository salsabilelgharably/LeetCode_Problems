class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c =0
        res = []
        for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[j] < nums[i]:
                        c +=1
                res.append(c)
                c=0
        return res      
        