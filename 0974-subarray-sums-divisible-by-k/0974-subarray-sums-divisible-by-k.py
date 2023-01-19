class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        res=0
        temp=0
        for i in nums:
            temp+=i
            rem=temp%k
            if rem<0:
                rem+=k
            if rem in d:
                res+=d[rem]
                d[rem]+=1
            else:
                d[rem]=1
        return res