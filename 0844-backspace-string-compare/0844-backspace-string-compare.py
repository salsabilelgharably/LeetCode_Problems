class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_copy=[]
        t_copy=[]
        for i in range(len(s)):
            if s[i] == '#' and len(s_copy) != 0:
                s_copy.pop()
            elif s[i] != '#':
                s_copy.append(s[i])

        for i in range(len(t)):
            if t[i] == '#'  and len(t_copy) !=0:
                t_copy.pop()
            elif t[i] != '#':
                t_copy.append(t[i])
        
        return s_copy == t_copy
                