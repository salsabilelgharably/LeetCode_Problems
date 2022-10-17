class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        res = []
        for i in arr:
            if arr.count(i) == 1:
                res.append(i)
        if len(res) < k:
            return ""
        else:
            return res[k-1]