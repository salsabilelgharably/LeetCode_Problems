class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for isin in words:
            for word in words:
                if isin == word:
                    continue
                if isin in word:
                    res.append(isin)
                    break
        return res