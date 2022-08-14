class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count = 0
        res = ''
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
                if count == k :
                    return res
            if count < k and i == len(s)-1:
                return s
            res += s[i]