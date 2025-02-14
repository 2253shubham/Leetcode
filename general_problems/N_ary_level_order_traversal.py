# Problem description here https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        k = deque([root])
        out = []

        while k:
            curl = []
            ls = len(k)
            for _ in range(ls):  # Process all nodes at the current level
                node = k.popleft()  # Pop from the front
                curl.append(node.val)
                if node.children:
                    k.extend(node.children)  # Add children to queue

            out.append(curl)  # Store level-wise values

        return out


# Time Complexity = O(N), Space complexity = O(N)
