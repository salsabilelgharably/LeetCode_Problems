class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = []
        for word in words:
            for row in rows:
                if all(letter in row for letter in word.lower()):
                    res.append(word)
        return res