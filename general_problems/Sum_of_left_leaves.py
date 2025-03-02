# Problem description here https://leetcode.com/problems/sum-of-left-leaves/description/
# Solved using BFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leaves = deque([root])
        sumn = 0
        while leaves:
            cur_node = leaves.pop()

            if cur_node.left and not cur_node.left.left and not cur_node.left.right:
                sumn += cur_node.left.val

            if cur_node.left:
                leaves.append(cur_node.left)
            
            if cur_node.right:
                leaves.append(cur_node.right)
        
        return sumn
    

# Time Complexity = O(N), Space Complexity = O(N)

"""

# Alternate solution using DFS (Better Space complexity of O(1))

from typing import Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_sum = 0
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val

        return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

"""