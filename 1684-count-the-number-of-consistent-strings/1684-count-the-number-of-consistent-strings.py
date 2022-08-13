class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = [*allowed]
        count = 0
        for word in words:
            if set(word).issubset(allow) == True:
                count +=1
                
        return count