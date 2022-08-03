class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if s=='' or t == "":
            return True
        for i in range(len(t)):
            if s[0] == t[i]:
                s = s[1:]
                if s =='':
                    return True
        return False
        