class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        res = 0
        for word in min(words1,words2):
            if words1.count(word) == 1 and words2.count(word) == 1:
                res += 1
        return res