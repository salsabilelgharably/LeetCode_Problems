class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        if len(s) % 2 == 0:
            for i in range(0, len(s), 2):
                res += s[i] + chr( ord(s[i]) + int(s[i+1]))
        else:
            for i in range(0, len(s) -2 , 2):
                res += s[i] + chr( ord(s[i]) + int(s[i+1]))
            res += s[-1]
        return res                        