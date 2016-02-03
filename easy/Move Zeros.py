class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.solution2(nums)
    
    def solution1(self, nums):
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

    def solution2(self, nums):
        zero_counter = 0
        i = 0
        while i < len(nums)-zero_counter:
            if nums[i] == 0:
                    # 如果遇到0就往前shift
                nums[i:-zero_counter-1] = nums[i+1:len(nums)-zero_counter]
                # 紀錄尾巴的地方要塞幾個零，len(nums)-zero_counter也是新的邊界所在
                zero_counter += 1
            else:
                # 如果非0的話就要繼續看一下一個
                    i += 1
            # 用0把尾巴填滿
            nums[-zero_counter:] = [0 for i in range(zero_counter)] if zero_counter > 0 else nums
