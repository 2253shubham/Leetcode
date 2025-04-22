# Problem description here https://leetcode.com/problems/diameter-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longl = 0

        def dfs(node):
            nonlocal longl

            if node == None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            longl = max(longl, left + right)
            return 1 + max(left, right)

        dfs(root)
        return longl


# Time Complexity = O(N), Space Complexity = O(N)
