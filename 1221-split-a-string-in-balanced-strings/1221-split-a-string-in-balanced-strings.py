class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        List_RL = []
        s_RL = ""
        num_R = 0
        num_L = 0        
        for i in range(len(s)):
            if s[i] == "R":
                s_RL += s[i]
                num_R += 1
            elif s[i] == "L":
                s_RL += s[i]
                num_L += 1
            if num_R == num_L:
                List_RL.append(s_RL)
                s_RL = ""
                num_R =0
                num_L =0
        return len(List_RL)
                