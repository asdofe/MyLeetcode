class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        zero = 0
        # 迴圈終點
        while non_zero < len(nums) and zero < len(nums):
            # 找到第1個0的位置
            while zero < len(nums) and nums[zero] != 0:
                zero += 1
                
            non_zero = zero + 1
            # 找到第1個非0的位置
            while non_zero < len(nums) and nums[non_zero] == 0:
                non_zero += 1
            # 互換位置
            if zero < len(nums) and non_zero < len(nums):
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero] 
            
            # 下一個尋找的起始點
            zero += 1