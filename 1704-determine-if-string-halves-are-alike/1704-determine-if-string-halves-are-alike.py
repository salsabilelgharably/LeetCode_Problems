class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l = len(s)
        a,b=0,0
        for i in s[:l/2]:
            if i in vowels:
                a += 1
        for i in s[l/2:]:
            if i in vowels:
                b += 1
        return a == b