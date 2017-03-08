# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a1 = []
        a2 = []
        while l1 != None:
        	a1.append(l1.val)
        	l1 = l1.next
        while l2 != None:
        	a2.append(l2.val)
        	l2 = l2.next

        ret = []
        if len(a1) < len(a2):
        	a1, a2 = a2,a1
        s1 = len(a1)
        s2 = len(a2)
        s = 0
        for x in range(0, s2):
        	s = s + a1[x] + a2[x]
        	ret.append(s%10)
        	s = s/10

        for x in range(s2, s1):
        	s = s + a1[x] 
        	ret.append(s%10)
        	s = s/10

        if s>0:
        	ret.append(s)

        head = None
        l = None
        for x in ret:
        	if l == None:
        		l = ListNode(x)
        		head = l
        	else:
        		l.next = ListNode(x)
        		l = l.next
        return head