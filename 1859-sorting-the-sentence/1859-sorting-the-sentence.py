class Solution:
    def sortSentence(self, s: str) -> str:
        word = {}
        for i in s.split():
            word[int(i[-1])] = i[:-1]
        return " ".join([word[n] for n in range(1, len(word)+1)])
            
        