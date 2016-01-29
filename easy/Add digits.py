class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # num 除9餘 0 則 num = 0 則答案是0
                       # num != 0 則答案是9
        # num 除9不餘0 則 num除9餘數即為所求
        return num%9 if num%9 != 0 else( 0 if num == 0 else 9) Add digits