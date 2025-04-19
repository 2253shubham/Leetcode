# Problem description here https://leetcode.com/problems/evaluate-boolean-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> bool:
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            elif node.val == 3:
                return dfs(node.left) and dfs(node.right)

        return dfs(root)


# Time Complexity = O(N), Space Complexity = O(N)
