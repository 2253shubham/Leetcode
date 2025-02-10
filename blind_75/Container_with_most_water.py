# Problem description here https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        left = 0
        right = len(height) - 1
        dis = len(height) - 1
        max_vol = min(height[left], height[right]) * dis
        while left != right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            dis -= 1
            if min(height[left], height[right]) * dis > max_vol:
                max_vol = min(height[left], height[right]) * dis

        return max_vol


# Time Complexity = O(N), Space Complexity = O(1)
