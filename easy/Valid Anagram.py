class Solution(object):
    def isAnagram(self, s, t):
        # 把重複的字過濾掉
        li = set(s) if len(s) > len(t) else set(t)
        # 計算每個字出現的次數一布一樣
        for x in li:
            if s.count(x) != t.count(x):
                return False
        
        return True