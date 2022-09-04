class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        l=len(arr)
        count=0
        for i in range(l+1):
            if i%2==0:
                continue
            le=0
            r=i
            for j in range(l):
                if r<=l:
                    count+=sum(arr[le:r])
                    le+=1
                    r+=1
                else : break
        return count