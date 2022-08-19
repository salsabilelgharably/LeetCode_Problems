class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i:i+k] for i in range(0, len(s), k)]
        x = len(res[-1])
        if x < k :
            for x in range(k-x):
                res[-1] += fill
        return res