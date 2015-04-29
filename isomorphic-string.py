#-*- coding: utf8
class Solution:

    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
    	ms = {}
    	ts = {}
    	i = 0
    	s1 = []
    	s2 = []
    	for c in s:
    		if c not in ms:
    			ms[c] = i
    			i = i + 1
    		s1.append(ms[c])

    	i = 0
    	for c in t:
    		if c not in ts:
    			ts[c] = i
    			i = i + 1
    		s2.append(ts[c])
    	return s1 == s2


