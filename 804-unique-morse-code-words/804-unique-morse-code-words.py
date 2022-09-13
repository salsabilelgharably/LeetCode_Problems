class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformation =[]
        curWord = ''
        if len(words) == 1:
            return 1
        for word in words:
            for i in word:
                curWord += morse[ord(i) - 97]
            transformation.append(curWord)
            curWord = ''
        return len(set(transformation))               
        