class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=3:
            return True
        if n % 4 == 0:
            return False
        return True