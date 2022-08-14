class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        if s:
            s = s.split(" ")
            s = " ".join(s[0:k])
        return s