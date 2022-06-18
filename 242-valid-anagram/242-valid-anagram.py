class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uni_List = set(t)
        
        if len(s) != len(t):
            return False

        for i in uni_List:
            if t.count(i) != s.count(i):
                return False
        return True