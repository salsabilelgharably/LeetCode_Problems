class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = []
        for i in s:
        #check if i in list res[]
            if i in res:
                return i
            res.append(i)