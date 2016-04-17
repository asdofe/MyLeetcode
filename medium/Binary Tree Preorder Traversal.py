#Binary Tree Preorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.tree_nodes = []
        self.pre_tree_traverse(root)
        
        return self.tree_nodes
    
    def pre_tree_traverse(self, root):
        
        if root == None:
            return 
        
        self.tree_nodes += [root.val]
        
        self.pre_tree_traverse(root.left)
        self.pre_tree_traverse(root.right)
        
        
        
        