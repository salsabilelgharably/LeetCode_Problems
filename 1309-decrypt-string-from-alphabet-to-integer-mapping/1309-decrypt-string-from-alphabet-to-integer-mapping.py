class Solution:
    def freqAlphabets(self, s: str) -> str:
        spilt_s=s.split('#')
        res = ''
        for i in spilt_s:
            if len(i) == 2 or len(i) == 1:
                res += chr(96+int(i))
            elif len(i)>2:
                last = i[-2]+i[-1]
                for c in range(len(i)-2):
                    res += chr(96+int(i[c]))
                res += chr(96+int(last))
        if s[-1]  != '#':
            res = res[:-1]
            for i in spilt_s[-1]:
                res += chr(96+int(i))  
 
        return res