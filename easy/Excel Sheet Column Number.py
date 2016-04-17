class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        radix = 26
        base = 1
        s = s[::-1]
        for idx, str in enumerate(s):
            
            result += base * (ord(str) - 64)
            base *= radix
        return result 
        