#Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        self.nodes_list = []
        self.inorder_traverse(root)
        return self.nodes_list
        
    def inorder_traverse(self, root):
        
        if root == None:
            return 
        
        self.inorder_traverse(root.left)
        self.nodes_list += [root.val]
        self.inorder_traverse(root.right)