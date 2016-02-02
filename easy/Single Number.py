class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # xor有交換律，把全部的數xor起來即為所求
        return reduce(lambda a, b: a^b, nums)
