# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 如果root有東西的或者是root的左子樹或右子樹的其中一個有東西
        # 則把他的左右子樹對調
        # 然後再把左子樹和右子樹分別當root去做invert的動作
        if root and (root.left or root.right):
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root