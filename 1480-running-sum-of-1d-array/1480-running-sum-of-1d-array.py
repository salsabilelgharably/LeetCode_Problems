class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list_sum = nums
        Num_sum =0
        for i in range(len(list_sum)):
            Num_sum += list_sum[i]
            list_sum[i] = Num_sum 
        return list_sum