class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split()
        res = len(words)
        isin = False 
        for word in words:
            for letter in brokenLetters:
                if letter in word:
                    isin = True
                    break
                else:
                    isin = False 
            if isin:
                res -= 1
        return res