class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = Counter(s)
        for i in s:
            if l[i] == 1:
                return s.find(i)
        return -1