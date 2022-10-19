class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        res = 0
        while min(num1, num2) != 0:
            res += 1
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return res