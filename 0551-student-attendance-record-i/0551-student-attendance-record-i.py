class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        if len(s) < 3:
            return True
        for i in range(1, len(s)-1):
            if s[i-1] == s[i] == s[i+1] =='L':
                return False
        return True
        