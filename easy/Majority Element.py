class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = list(set(nums))
        num_max_count = 0
        num_max = 0
        for ns in nums_set:
            if nums.count(ns) > num_max_count:
                num_max_count = nums.count(ns)
                num_max = ns
            
        return num_max