class Solution(object):
    
    def nim_game(self,n):
        # 如果除4餘0就表示必輸
        if n%4 == 0:
            return False
        else :
            return True
        
        
    
    
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return self.nim_game(n)