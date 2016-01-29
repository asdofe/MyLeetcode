# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # md(x) = 0 ,如果 x 是 空
        #       = 1 ,如果 x 的 left和right都是空
        #       = 1 + max(md(x.left), md(x.right)) ,如果不是上面兩個狀況 
        md = lambda x: 0 if not x else 1 if x.left == None and x.right == None else 1 + max(md(x.left), md(x.right))
        return md(root)