# Problem description here https://leetcode.com/problems/course-schedule/description/

# 1) My solution with DFS

from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list for prerequisites
        course_map = defaultdict(set)
        for course, prereq in prerequisites:
            course_map[course].add(prereq)

        visited = set()  # To detect cycles

        def dfs(course):
            if course in visited:  # Cycle detected
                return False
            if not course_map[course]:  # No prerequisites left, safe to take
                return True

            visited.add(course)
            for prereq in course_map[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)  # Remove from cycle detection set
            course_map[course] = set()  # Mark course as completed

            return True

        # Check for cycles in each course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


# Time Complexity = O(N + E), Space Complexity = O(N + E)
# where N is the number of courses and E is the number of prerequisites pairs

# Alternative solutions

# 2) BFS with Kahn's Algorithm


class Solution:
    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList

    def topoBFS(self, numNodes, edgesList):
        # Note: for consistency with other solutions above, we keep building
        # an adjacency list here. We can also merge this step with the next step.
        adjList = self.buildAdjacencyList(numNodes, edgesList)

        # 1. A list stores No. of incoming edges of each vertex
        inDegrees = [0] * numNodes
        for v1, v2 in edgesList:
            # v2v1 form a directed edge
            inDegrees[v1] += 1

        # 2. a queue of all vertices with no incoming edge
        # at least one such node must exist in a non-empty acyclic graph
        # vertices in this queue have the same order as the eventual topological
        # sort
        queue = []
        for v in range(numNodes):
            if inDegrees[v] == 0:
                queue.append(v)

        # initialize count of visited vertices
        count = 0
        # an empty list that will contain the final topological order
        topoOrder = []

        while queue:
            # a. pop a vertex from front of queue
            # depending on the order that vertices are removed from queue,
            # a different solution is created
            v = queue.pop(0)
            # b. append it to topoOrder
            topoOrder.append(v)

            # increase count by 1
            count += 1

            # for each descendant of current vertex, reduce its in-degree by 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                # if in-degree becomes 0, add it to queue
                if inDegrees[des] == 0:
                    queue.append(des)

        if count != numNodes:
            return None  # graph has at least one cycle
        else:
            return topoOrder

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topoBFS(numCourses, prerequisites) else False


# Time Complexity = O(N + E), Space Complexity = O(N + E)
# where N is the number of courses and E is the number of prerequisites pairs
