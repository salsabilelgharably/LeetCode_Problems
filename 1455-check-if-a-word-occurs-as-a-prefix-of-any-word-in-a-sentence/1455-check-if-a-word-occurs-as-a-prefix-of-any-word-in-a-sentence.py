class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word = sentence.split()
        for i in word:
            if i[:len(searchWord)] == searchWord:
                return word.index(i) + 1
        return -1