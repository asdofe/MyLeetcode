# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 把自己的下一個節點拉過來取代自己
        # 意義上就是把下一個節點幹掉的意思
        node.val = node.next.val
        node.next = node.next.next