class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        alphabet = []
        for i in range(97, 123):
            alphabet.append(chr(i))
        for x in alphabet:
            if sentence.find(x) == -1:
                return False
        return True
        