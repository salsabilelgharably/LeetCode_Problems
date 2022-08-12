class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alpha = []
        x = ''
        for i in range(ord(s[0]), ord(s[3]) + 1):
            x = chr(i)
            for n in range(int(s[1]), int(s[4]) + 1):
                x += str(n)
                alpha.append(x)
                x = x[0]
            x =''
        return alpha