class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        
        for c in s:
            if s.isdigit(): num+=c
            else:
                num += str(ord(c)-ord('a')+1)
        
        for _ in range(k):
            n = 0
            for c in num:
                n += int(c)
            
            num = str(n)
            
        return int(num)