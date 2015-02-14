class Solution:
    def compare(self, a, b):
        sa = str(a)
    	sb = str(b)
    	ta = sa + sb
    	tb = sb + sa
    	lenght = len(ta)
    	i = 0
    	while i<lenght:
    		if ta[i] < tb[i]:
    			return -1
    		elif ta[i] > tb[i]:
    			return 1
    		i = i + 1
    	return 0
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num.sort(cmp=self.compare, reverse=True)
        ret = "".join(str(i) for i in num)
        if ret[0] == '0':
            return '0'
        return ret