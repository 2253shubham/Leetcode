# Problem description here https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        q = deque([node])
        clones = {node.val: Node(node.val, [])}

        while q:
            curr = q.popleft()
            curr_clone = clones[curr.val]

            for i in curr.neighbors:
                if i.val not in clones:
                    clones[i.val] = Node(i.val, [])
                    q.append(i)

                curr_clone.neighbors.append(clones[i.val])

        return clones[node.val]
    
# Time Complexity = O(N + E), Space Complexity = O(N + E)
# where N is the number of nodes and E is the number of edges in the graph
