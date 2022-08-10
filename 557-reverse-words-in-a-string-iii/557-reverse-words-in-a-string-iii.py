class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res =''
        x = 0
        for i in s:
            x = len(i)
            while x > 0:
                res += i[x-1]
                x -= 1
            res += ' '

        return res[:-1]
        