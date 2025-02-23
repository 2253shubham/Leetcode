# Problem description here https://leetcode.com/problems/perfect-rectangle/description/

from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        from collections import defaultdict
        
        point_count = defaultdict(int)
        area_sum = 0
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')

        for x1, y1, x2, y2 in rectangles:
            area_sum += (x2 - x1) * (y2 - y1)

            # Update the bounding rectangle
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)

            # Track the occurrence of each corner
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                point_count[point] += 1

        # The total area must match the bounding rectangle area
        if area_sum != (max_x - min_x) * (max_y - min_y):
            return False

        # The four bounding corners should appear exactly once
        corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        for corner in corners:
            if point_count.pop(corner, 0) != 1:
                return False

        # All other points should appear even times (ensuring proper tiling)
        return all(v % 2 == 0 for v in point_count.values())

# Time Complexity = O(N), Space Complexity = O(N)