# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
   
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #inorder 和preorder或postorder可以表示出一顆唯一的binary tree
        #inorder traversal
        inorder = lambda r: [None] if not r else inorder(r.left) + [r.val] + inorder(r.right)
        #preorder traversal
        preorder = lambda r: [None] if not r else [r.val] + preorder(r.left) + preorder(r.right)
        #比較兩個list是否相等
        diff_list = lambda a, b: True if len(a) == len(b) and len([(x, y) for x, y in zip(a, b) if x!=y]) == 0 else False

        if diff_list(inorder(p), inorder(q)) and diff_list(preorder(p), preorder(q)):
            return True
        else:
            return False
