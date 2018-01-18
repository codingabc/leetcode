class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 0
        s = 1
        if x < 0:
        	x = -x
        	s = -1
        while x!=0:
        	n = n*10+x%10
        	x = x/10

        n = n * s
        if n < -0x7fffffff or n > 0x80000000:
        	return 0
        return n



if __name__ == "__main__":
	a = Solution()
	print(a.reverse(123))
	print(a.reverse(-123))
	print(a.reverse(120))
	print(a.reverse(1534236469))
