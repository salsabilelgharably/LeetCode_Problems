class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) ==1 or max(nums) == 0 :
            return 1
        
        uni_list=[]
        for num in nums:
            if num not in uni_list:
                uni_list.append(num)
        
        last = uni_list[1] - uni_list[0]
        current = 0
        li=[uni_list[0], uni_list[1]]

        
        for i in range(1, len(nums)):
            current = nums[i] - nums[i-1]
            if current * last < 0:
                li.append(nums[i])
                last = current
                
        return len(li)
            