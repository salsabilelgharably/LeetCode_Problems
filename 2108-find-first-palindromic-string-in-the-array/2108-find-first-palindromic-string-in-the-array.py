class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        x =False
        for word in words:
            if len(word) == 1:
                return word
            for i in range(int(len(word)/2)) : 
                if word[i] == word[len(word) -1 - i]:
                    x = True
                else:
                    x = False
                    break
            if x == True:
                return word        
        return ""