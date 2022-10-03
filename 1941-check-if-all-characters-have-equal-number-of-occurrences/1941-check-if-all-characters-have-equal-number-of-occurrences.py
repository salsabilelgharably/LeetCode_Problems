class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = False
        last = s.count(s[0])
        now = last
        for char in set(s):
            now = s.count(char)
            if last == now:
                res=True
                last = now
            else:
                return False
        return res            