class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        test1 = multi_array(nums)
	   # print(test1.mul_val)
        return test1.mul()

import random

class multi_array:
    
    def __init__(self, inp):
        self.random_array = inp[:]
        self.output_ranodm_array = self.random_array[::-1]
        # print(self.random_array)
        # print(self.output_ranodm_array)
        # self.mul_val = self.mul()


    def mul(self):
        
        temp1, temp2 = 1, 1
        # print(self.random_array)
        # print(self.output_ranodm_array)
        for idx, ele in enumerate(self.random_array):
            temp1, self.random_array[idx] = self.random_array[idx], temp1
            temp1 = temp1 * self.random_array[idx]
            temp2, self.output_ranodm_array[idx] = self.output_ranodm_array[idx], temp2
            temp2 = temp2 * self.output_ranodm_array[idx]
        self.output_ranodm_array = self.output_ranodm_array[::-1]
        # print(self.random_array)
        # print(self.output_ranodm_array)
        

        return list(map(lambda a,b : a*b ,self.random_array, self.output_ranodm_array ))

