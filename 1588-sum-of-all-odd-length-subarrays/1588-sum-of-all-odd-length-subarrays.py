class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        Sum=0
        for i in range(len(arr)):
               Sum += ((((i + 1) *(len(arr) - i) +1) // 2) * arr[i])
        return Sum