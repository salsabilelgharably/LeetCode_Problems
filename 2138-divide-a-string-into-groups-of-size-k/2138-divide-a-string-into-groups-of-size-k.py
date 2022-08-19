class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i:i+k] for i in range(0, len(s), k)]
        if len(res[-1]) < k :
            for i in range(k-len(res[-1])):
                res[-1] += fill
        return res