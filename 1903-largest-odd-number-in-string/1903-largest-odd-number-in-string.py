class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = num[::-1]
        nums = ['1', '3', '5', '7', '9']
        closest_index = len(num)
        for i in nums:
            ind = num.find(i)
            if ind != -1 and closest_index > ind:
                closest_index = ind
        return num[closest_index:][::-1]