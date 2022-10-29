class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if str(num)[-1] != '0' or num == 0:
            return True
        else:
            return False