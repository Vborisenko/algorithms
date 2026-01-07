from typing import Optional


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def return_sum(root_node: TreeNode):
            sum = 0

            if low <= root_node.val <= high:
                sum += root_node.val

            if root_node.left:
                sum += return_sum(root_node.left)
            if root_node.right:
                sum += return_sum(root_node.right)

            return sum

        return return_sum(root)
