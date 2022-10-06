class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res =0
        isin=False
        for word in words:
            for char in word:
                if chars.count(char) >= word.count(char):
                    isin = True
                else:
                    isin = False
                    break
            if isin == True:
                res += len(word)
        return(res)