class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        i = 0
        j = len(s)-1
        sign = 1
        if s[0] == '-':
        	sign = -1
        	i = 1

        while j>=i:
        	if s[j] != '0':
        		break
        	j = j - 1

        n = 0
        while j>=i:
        	n = n + int(s[j]) * (10**(j-i))
        	j = j - 1

        n = sign* n
        if n >= -0x7fffffff and n <= 0x80000000:
        	return n
        return 0



if __name__ == "__main__":
	a = Solution()
	print(a.reverse(123))
	print(a.reverse(-123))
	print(a.reverse(120))
	print(a.reverse(1534236469))
