class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        res = 0
        l = len(pref)
        for i in words:
            if l <= len(i):
                if pref == i[:l]:
                    res += 1
        return res