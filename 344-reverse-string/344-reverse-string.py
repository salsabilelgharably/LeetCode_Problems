class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 1
        right = 1
        s_len = len(s)
        while left + right <= s_len:
            s[left-1], s[s_len-right] = s[s_len-right], s[left-1]
            left += 1
            right += 1