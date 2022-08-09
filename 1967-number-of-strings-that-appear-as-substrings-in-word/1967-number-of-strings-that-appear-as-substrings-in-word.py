class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for i in patterns:
            if word.find(i) != -1:
                res +=1
        return res