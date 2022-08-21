class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0,len(s),2*k):
            s =s[:i] + ''.join(reversed(s[i:i+k])) + s[i+k:]
        return s
        