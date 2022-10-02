class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ''
        c1, c2 = 0, 0
        l1 = len(word1)
        l2 = len(word2)
        for i in range(max(l1, l2)):
            if l1 > c1:
                res += word1[c1]
                c1 += 1
            if l2 > c2:
                res += word2[c2]
                c2 += 1
        return res