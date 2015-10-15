class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        n = len(nums)
        for i in range(0, n):
            x = target - nums[i]
            if x in d:
                return [d[x]+1, i+1]
            else:
                d[nums[i]] = i
        return [0, 0]